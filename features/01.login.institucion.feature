Feature: Login Institucion

  Scenario: Login Error as Institucion on /institucion
    Given Load the Uri /institucion
    When Click by Link Text Ingresa
    When Fill field by ID txtUser with miinstitucion@miemail.com
    When Fill field by ID txtPasswordLogin with Clave101
    When Click by Id btnLoginUser
    When Wait 5 seconds
    Then Should redirect to /institucion

  Scenario Outline: Login succesful as Institucion on /institucion
    Given Load the Uri /institucion
    When Click by Link Text Ingresa 
    When Fill field by ID txtUser with <usuario>
    When Fill field by ID txtPasswordLogin with <clave>
    When Click by Tag Text button with Ingresar
    When I wait 5 seconds until see text Mi Cuenta
    Then Should redirect to /institucion/mi-cuenta

    Examples: Usuario
    | usuario                   | clave      |
    | instituto60@email.com.pe  | ClaveVa101 |

