# -*- coding: UTF-8 -*-

"""
based on from github "https://gist.github.com/s1ider/f13c2f163282dbec7a61"
Customized for parallel scenarios
Authors: i4s-pserrano
"""

from multiprocessing import Pool
from subprocess import Popen, PIPE
from subprocess import check_output, STDOUT, CalledProcessError, TimeoutExpired
from glob import glob
import logging
import argparse
import json
import sys
from functools import partial
from datetime import datetime

logging.basicConfig(level=logging.INFO,
                    format="[%(levelname)-8s %(asctime)s] %(message)s")
logger = logging.getLogger(__name__)

delimiter = "_BEHAVE_PARALLEL_BDD_"

start_time = datetime.now()

def parse_arguments():
    """
    Parses commandline arguments
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser('Run behave in parallel mode for scenarios')
    parser.add_argument('--processes', '-p', type=int, help='Maximum number of processes. Default = 5', default=5)
    parser.add_argument('--tags', '-t', help='specify behave tags to run')
    parser.add_argument('--timeout', '-tout', type=int,
                        help='Maximum seconds to execute each scenario. Default = 300', default=300)
    args = parser.parse_args()
    return args


def _run_feature(feature_scenario, timeout):
    """
    Runs features/scenarios
    :param feature_scenario: Feature/scenario that should be run
    :type feature_scenario: str
    :return: Feature/scenario and status
    """
    execution_code = {0: 'OK', 1: 'FAILED', 2: 'TIMEOUT'}
    execution_elements = feature_scenario.split(delimiter)
    logger.debug("Processing feature: {} and scenario {}".format(execution_elements[0], execution_elements[1]))
    params = "--no-capture"
    cmd = "behave --no-summary -k --no-junit -f plain {0} -i {1} --name \"{2}\" -o \"./reports/{1}/{2}.out\"".format(
           params, execution_elements[0], execution_elements[1])
    try:
        r = check_output(cmd, shell=True, timeout=timeout)
        code = 0
    except CalledProcessError as e:
        out_bytes = e.output
        code = e.returncode
    except TimeoutExpired:
        code = 2
    status = execution_code[code]
    logger.info("{0:50}: {1} --> {2}".format(execution_elements[0], execution_elements[1], status))
    return execution_elements[0], execution_elements[1], status


def main():
    """
    Runner
    """
    args = parse_arguments()
    pool = Pool(args.processes)
    if args.tags:
        cmd = 'behave -d --no-junit --f json --no-summary -t {}'.format(args.tags)
    else:
        cmd = 'behave -d --no-junit --f json --no-summary'

    p = Popen(cmd, stdout=PIPE, shell=True)
    out, err = p.communicate()
    try:
        j = json.loads(out.decode())
    except ValueError:
        j = []
    features = [e['location'].replace(r'features/', '')[:-2] for e in j]



    # features dictionary with scenarios
    features_scenarios = [[e['location'].replace(r'features/', '')[:-2] + delimiter + i['name']
                                for i in e['elements']
                                    if i['keyword'].upper() in ["scenario".upper(), "scenario outline".upper()]]
                            for e in j]

    features_and_scenarios = []
    for elto in features_scenarios:
        features_and_scenarios = features_and_scenarios + elto

    logger.info("Found {} features".format(len(features)))
    logger.info("Found {} scenarios".format(len(features_and_scenarios)))
    logger.info("Timeout for each scenario {} seconds".format(args.timeout))
    if args.processes > len(features_and_scenarios):
        logger.info("You have defined {} and Will execute only necessary {} parallel process ".format(args.processes,
                                                                                        len(features_and_scenarios)))
    else:
        logger.info("Will execute {} parallel process".format(args.processes))

    run_feature = partial(_run_feature, timeout=args.timeout)
    logger.info("--------------------------------------------------------------------------")
    output = 0
    for feature, scenario, status in pool.map(run_feature, features_and_scenarios):
        if status != 'OK':
            if output == 0:
                if status == "FAILED":
                    output = 1
                else:
                    output = 2
    logger.info("--------------------------------------------------------------------------")
    end_time = datetime.now()

    logger.info("Duration: {}".format(format(end_time - start_time)))

    sys.exit(output)

if __name__ == '__main__':
    main()
