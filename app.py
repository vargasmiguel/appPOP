import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pandas import Timestamp

st.set_page_config(layout='wide',
                           page_title="Informe Orientación Profesional",
                           page_icon="🚀")

st.html("""<style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """)

habilidades_iconos = {
    'Capacidad lingüística':'fas fa-language',
    'Observación y análisis': 'fas fa-search',
    'Abstracción': 'fas fa-lightbulb',
    'Analizador': 'fas fa-microscope',
    'Perceptivo y manual': 'fas fa-hand-paper',
    'Trabajo en equipo': 'fas fa-users',
    'Pensamiento critico': 'fas fa-brain',
    'Responsabilidad social': 'fas fa-handshake',
    'Creatividad': 'fas fa-paint-brush',
    'Memoria': 'fas fa-memory',
    'Sentido de cooperación': 'fas fa-hands-helping',
    'Organización planificación': 'fas fa-tasks',
    'Razonamiento abstracción': 'fas fa-puzzle-piece',
    'Método científico': 'fas fa-flask',
    'Razonamiento numérico': 'fas fa-calculator',
    'Destreza manual': 'fas fa-tools',
    'Sensibilidad artística y cultural': 'fas fa-palette',
    'Comunicación social': 'fas fa-comments',
    'Análisis y síntesis': 'fas fa-chart-pie',
    'Adaptación al cambio': 'fas fa-sync-alt'
}

gustos_iconos = {
    'Teatro': 'fas fa-theater-masks',
    'Maquinas': 'fas fa-cogs',
    'Fenómenos sociales': 'fas fa-users',
    'Gusto por el cambio': 'fas fa-sync-alt',
    'Avances TIC gadgets': 'fas fa-mobile-alt',
    'Investigación': 'fas fa-search',
    'Museos': 'fas fa-landmark',
    'Ideas nuevas': 'fas fa-lightbulb',
    'Amistades': 'fas fa-user-friends',
    'Estatus': 'fas fa-trophy',
    'Cuerpo humano': 'fas fa-user',
    'Lujos': 'fas fa-gem',
    'Innovación': 'fas fa-rocket',
    'Trabajo de campo': 'fas fa-tractor',
    'Funcionamiento de las cosas': 'fas fa-cog',
    'Nutricional': 'fas fa-apple-alt',
    'Servicio a la comunidad': 'fas fa-hands-helping',
    'Video Juegos': 'fas fa-gamepad',
    'Difusión de la cultura': 'fas fa-bullhorn',
    'Como funcionan las cosas': 'fas fa-tools',
    'Concepto de la vida y sus procesos': 'fas fa-dna',
    'Números': 'fas fa-calculator',
    'Lectura': 'fas fa-book',
    'Relaciones personales': 'fas fa-handshake',
    'Laboratorios': 'fas fa-flask',
    'Aire libre': 'fas fa-tree',
    'Cine arte': 'fas fa-film',
    'Cultura': 'fas fa-globe',
    'Naturaleza': 'fas fa-leaf',
    'Apreciación estética': 'fas fa-palette',
    'Dinero': 'fas fa-dollar-sign'
}

@st.cache_data
def data():
  di={'documento': {0: 1061278936, 1: 1087999846, 2: 1088828127, 3: 1088830631, 4: 1088830631, 5: 1088829426, 6: 1088277552, 7: 1085717952, 8: 1085717952, 9: 1088830631, 10: 1085719045, 11: 1028840396, 12: 1088829994, 13: 1016597101, 14: 1088830007, 15: 1088829994, 16: 1088827346, 17: 1085719045, 18: 1088829994, 19: 1088829994, 20: 1088828922, 21: 1085718595, 22: 1088830183, 23: 1085718833, 24: 1030140187, 25: 1088266252, 26: 1088828922, 27: 1031810271, 28: 1085718799, 29: 1088829540, 30: 1087551817, 31: 1089934081, 32: 1088831300, 33: 1089934428, 34: 1137059826, 35: 1089603933, 36: 1137059826, 37: 1137059826, 38: 1137059826, 39: 1088831104, 40: 1088831104, 41: 1088831341, 42: 1105371553, 43: 1089099976, 44: 1089099976, 45: 1089099835, 46: 1089098983, 47: 1089381794, 48: 1109545389, 49: 1089602535, 50: 1142515499, 51: 1089099724, 52: 1089603437, 53: 1088830845, 54: 1089935811, 55: 1089603478, 56: 1137060391, 57: 1089383954, 58: 1137060391, 59: 1088830944, 60: 1137060818, 61: 1089390618, 62: 1128848072, 63: 1089935832}, 'localidadId': {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 11: 4, 12: 4, 13: 4, 14: 4, 15: 4, 16: 4, 17: 4, 18: 4, 19: 4, 20: 4, 21: 4, 22: 4, 23: 4, 24: 4, 25: 4, 26: 4, 27: 4, 28: 4, 29: 4, 30: 4, 31: 4, 32: 4, 33: 4, 34: 4, 35: 4, 36: 4, 37: 4, 38: 4, 39: 4, 40: 4, 41: 4, 42: 4, 43: 4, 44: 4, 45: 4, 46: 4, 47: 4, 48: 4, 49: 4, 50: 4, 51: 4, 52: 4, 53: 4, 54: 4, 55: 4, 56: 4, 57: 4, 58: 4, 59: 4, 60: 4, 61: 4, 62: 4, 63: 4}, 'localidad': {0: 'otros', 1: 'otros', 2: 'otros', 3: 'otros', 4: 'otros', 5: 'otros', 6: 'otros', 7: 'otros', 8: 'otros', 9: 'otros', 10: 'otros', 11: 'otros', 12: 'otros', 13: 'otros', 14: 'otros', 15: 'otros', 16: 'otros', 17: 'otros', 18: 'otros', 19: 'otros', 20: 'otros', 21: 'otros', 22: 'otros', 23: 'otros', 24: 'otros', 25: 'otros', 26: 'otros', 27: 'otros', 28: 'otros', 29: 'otros', 30: 'otros', 31: 'otros', 32: 'otros', 33: 'otros', 34: 'otros', 35: 'otros', 36: 'otros', 37: 'otros', 38: 'otros', 39: 'otros', 40: 'otros', 41: 'otros', 42: 'otros', 43: 'otros', 44: 'otros', 45: 'otros', 46: 'otros', 47: 'otros', 48: 'otros', 49: 'otros', 50: 'otros', 51: 'otros', 52: 'otros', 53: 'otros', 54: 'otros', 55: 'otros', 56: 'otros', 57: 'otros', 58: 'otros', 59: 'otros', 60: 'otros', 61: 'otros', 62: 'otros', 63: 'otros'}, 'colegioId': {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6, 8: 6, 9: 6, 10: 6, 11: 6, 12: 6, 13: 6, 14: 6, 15: 6, 16: 6, 17: 6, 18: 6, 19: 6, 20: 6, 21: 6, 22: 6, 23: 6, 24: 6, 25: 6, 26: 6, 27: 6, 28: 6, 29: 6, 30: 6, 31: 6, 32: 6, 33: 6, 34: 6, 35: 6, 36: 6, 37: 6, 38: 6, 39: 6, 40: 6, 41: 6, 42: 6, 43: 6, 44: 6, 45: 6, 46: 6, 47: 6, 48: 6, 49: 6, 50: 6, 51: 6, 52: 6, 53: 6, 54: 6, 55: 6, 56: 6, 57: 6, 58: 6, 59: 6, 60: 6, 61: 6, 62: 6, 63: 6}, 'colegio': {0: 'María Dolorosa', 1: 'María Dolorosa', 2: 'María Dolorosa', 3: 'María Dolorosa', 4: 'María Dolorosa', 5: 'María Dolorosa', 6: 'María Dolorosa', 7: 'María Dolorosa', 8: 'María Dolorosa', 9: 'María Dolorosa', 10: 'María Dolorosa', 11: 'María Dolorosa', 12: 'María Dolorosa', 13: 'María Dolorosa', 14: 'María Dolorosa', 15: 'María Dolorosa', 16: 'María Dolorosa', 17: 'María Dolorosa', 18: 'María Dolorosa', 19: 'María Dolorosa', 20: 'María Dolorosa', 21: 'María Dolorosa', 22: 'María Dolorosa', 23: 'María Dolorosa', 24: 'María Dolorosa', 25: 'María Dolorosa', 26: 'María Dolorosa', 27: 'María Dolorosa', 28: 'María Dolorosa', 29: 'María Dolorosa', 30: 'María Dolorosa', 31: 'María Dolorosa', 32: 'María Dolorosa', 33: 'María Dolorosa', 34: 'María Dolorosa', 35: 'María Dolorosa', 36: 'María Dolorosa', 37: 'María Dolorosa', 38: 'María Dolorosa', 39: 'María Dolorosa', 40: 'María Dolorosa', 41: 'María Dolorosa', 42: 'María Dolorosa', 43: 'María Dolorosa', 44: 'María Dolorosa', 45: 'María Dolorosa', 46: 'María Dolorosa', 47: 'María Dolorosa', 48: 'María Dolorosa', 49: 'María Dolorosa', 50: 'María Dolorosa', 51: 'María Dolorosa', 52: 'María Dolorosa', 53: 'María Dolorosa', 54: 'María Dolorosa', 55: 'María Dolorosa', 56: 'María Dolorosa', 57: 'María Dolorosa', 58: 'María Dolorosa', 59: 'María Dolorosa', 60: 'María Dolorosa', 61: 'María Dolorosa', 62: 'María Dolorosa', 63: 'María Dolorosa'}, 'cursoId': {0: 22, 1: 22, 2: 22, 3: 22, 4: 22, 5: 22, 6: 22, 7: 22, 8: 22, 9: 22, 10: 22, 11: 22, 12: 22, 13: 22, 14: 22, 15: 22, 16: 22, 17: 22, 18: 22, 19: 22, 20: 22, 21: 22, 22: 22, 23: 22, 24: 22, 25: 22, 26: 22, 27: 22, 28: 22, 29: 22, 30: 22, 31: 22, 32: 22, 33: 22, 34: 22, 35: 22, 36: 22, 37: 22, 38: 22, 39: 22, 40: 22, 41: 22, 42: 22, 43: 22, 44: 22, 45: 22, 46: 22, 47: 22, 48: 22, 49: 22, 50: 22, 51: 22, 52: 22, 53: 22, 54: 22, 55: 22, 56: 22, 57: 22, 58: 22, 59: 22, 60: 22, 61: 22, 62: 22, 63: 22}, 'curso': {0: 'Test Vocacional', 1: 'Test Vocacional', 2: 'Test Vocacional', 3: 'Test Vocacional', 4: 'Test Vocacional', 5: 'Test Vocacional', 6: 'Test Vocacional', 7: 'Test Vocacional', 8: 'Test Vocacional', 9: 'Test Vocacional', 10: 'Test Vocacional', 11: 'Test Vocacional', 12: 'Test Vocacional', 13: 'Test Vocacional', 14: 'Test Vocacional', 15: 'Test Vocacional', 16: 'Test Vocacional', 17: 'Test Vocacional', 18: 'Test Vocacional', 19: 'Test Vocacional', 20: 'Test Vocacional', 21: 'Test Vocacional', 22: 'Test Vocacional', 23: 'Test Vocacional', 24: 'Test Vocacional', 25: 'Test Vocacional', 26: 'Test Vocacional', 27: 'Test Vocacional', 28: 'Test Vocacional', 29: 'Test Vocacional', 30: 'Test Vocacional', 31: 'Test Vocacional', 32: 'Test Vocacional', 33: 'Test Vocacional', 34: 'Test Vocacional', 35: 'Test Vocacional', 36: 'Test Vocacional', 37: 'Test Vocacional', 38: 'Test Vocacional', 39: 'Test Vocacional', 40: 'Test Vocacional', 41: 'Test Vocacional', 42: 'Test Vocacional', 43: 'Test Vocacional', 44: 'Test Vocacional', 45: 'Test Vocacional', 46: 'Test Vocacional', 47: 'Test Vocacional', 48: 'Test Vocacional', 49: 'Test Vocacional', 50: 'Test Vocacional', 51: 'Test Vocacional', 52: 'Test Vocacional', 53: 'Test Vocacional', 54: 'Test Vocacional', 55: 'Test Vocacional', 56: 'Test Vocacional', 57: 'Test Vocacional', 58: 'Test Vocacional', 59: 'Test Vocacional', 60: 'Test Vocacional', 61: 'Test Vocacional', 62: 'Test Vocacional', 63: 'Test Vocacional'}, 'jornadaId': {0: 10, 1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10, 10: 10, 11: 10, 12: 10, 13: 10, 14: 10, 15: 10, 16: 10, 17: 10, 18: 10, 19: 10, 20: 10, 21: 10, 22: 10, 23: 10, 24: 10, 25: 10, 26: 10, 27: 10, 28: 10, 29: 10, 30: 10, 31: 10, 32: 10, 33: 10, 34: 10, 35: 10, 36: 10, 37: 10, 38: 10, 39: 10, 40: 10, 41: 10, 42: 10, 43: 10, 44: 10, 45: 10, 46: 10, 47: 10, 48: 10, 49: 10, 50: 10, 51: 10, 52: 10, 53: 10, 54: 10, 55: 10, 56: 10, 57: 10, 58: 10, 59: 10, 60: 10, 61: 10, 62: 10, 63: 10}, 'jornada': {0: 'Mañana', 1: 'Mañana', 2: 'Mañana', 3: 'Mañana', 4: 'Mañana', 5: 'Mañana', 6: 'Mañana', 7: 'Mañana', 8: 'Mañana', 9: 'Mañana', 10: 'Mañana', 11: 'Mañana', 12: 'Mañana', 13: 'Mañana', 14: 'Mañana', 15: 'Mañana', 16: 'Mañana', 17: 'Mañana', 18: 'Mañana', 19: 'Mañana', 20: 'Mañana', 21: 'Mañana', 22: 'Mañana', 23: 'Mañana', 24: 'Mañana', 25: 'Mañana', 26: 'Mañana', 27: 'Mañana', 28: 'Mañana', 29: 'Mañana', 30: 'Mañana', 31: 'Mañana', 32: 'Mañana', 33: 'Mañana', 34: 'Mañana', 35: 'Mañana', 36: 'Mañana', 37: 'Mañana', 38: 'Mañana', 39: 'Mañana', 40: 'Mañana', 41: 'Mañana', 42: 'Mañana', 43: 'Mañana', 44: 'Mañana', 45: 'Mañana', 46: 'Mañana', 47: 'Mañana', 48: 'Mañana', 49: 'Mañana', 50: 'Mañana', 51: 'Mañana', 52: 'Mañana', 53: 'Mañana', 54: 'Mañana', 55: 'Mañana', 56: 'Mañana', 57: 'Mañana', 58: 'Mañana', 59: 'Mañana', 60: 'Mañana', 61: 'Mañana', 62: 'Mañana', 63: 'Mañana'}, 'nombre': {0: 'Sergio', 1: 'Kevin', 2: 'Sebastián', 3: 'Sara', 4: 'Sara', 5: 'Cristian', 6: 'Zara', 7: 'juan ', 8: 'juan ', 9: 'sara', 10: 'Juan', 11: 'Roberto', 12: 'Camila ', 13: 'Alejandra', 14: 'Isabel ', 15: 'Camila ', 16: 'Manuela', 17: 'Juan', 18: 'Camila ', 19: 'Camila ', 20: 'Sofia', 21: 'Laura', 22: 'Camila', 23: 'Natalia', 24: 'Simón', 25: 'Thomas', 26: 'Sofia', 27: 'Luis ', 28: 'samuel', 29: 'Emily', 30: 'Jerónimo ', 31: 'Steven', 32: 'Joham', 33: 'Jacobo', 34: 'Luna', 35: 'Santiago', 36: 'Luna', 37: 'Luna', 38: 'Luna', 39: 'Arawen', 40: 'Arawen', 41: 'David', 42: 'Ana Sofia', 43: 'Juan', 44: 'Juan', 45: 'Samuel', 46: 'Alejandro ', 47: 'Miguel', 48: 'Samuel', 49: 'Juan', 50: 'Heleen ', 51: 'Juan ', 52: 'Sofia ', 53: 'Alberto', 54: 'Thomas', 55: 'Santiago', 56: 'Valentina', 57: 'Jean Pool ', 58: 'Valentina', 59: 'Karen', 60: 'Juan ', 61: 'Victoria ', 62: 'treicy', 63: 'Sofia '}, 'apellido': {0: 'Solano', 1: 'Salazar', 2: 'Escobar', 3: 'Mahecha', 4: 'Mahecha', 5: 'Hernández ', 6: 'Muñoz', 7: 'mora', 8: 'mora', 9: 'Mahecha', 10: 'Zapata', 11: 'Solorzano', 12: 'Jaramillo ', 13: 'Rincón', 14: 'saraza', 15: 'Jaramillo ', 16: 'López', 17: 'Zapata', 18: 'Jaramillo ', 19: 'Jaramillo ', 20: 'Bedoya', 21: 'Rendon', 22: 'Hernández ', 23: 'Restrepo Osorio', 24: 'Vargas ', 25: 'Vargas', 26: 'Bedoya', 27: 'Suarez', 28: 'López', 29: 'Ramírez', 30: 'Villada ', 31: 'Toro', 32: 'Pérez', 33: 'Rendon ', 34: 'Isaza', 35: 'Salazar', 36: 'Isaza', 37: 'Isaza', 38: 'Isaza', 39: 'García', 40: 'García', 41: 'López', 42: 'Flores', 43: 'Gill', 44: 'Gill', 45: 'Campos', 46: 'Salazar ', 47: 'Castro', 48: 'Arbeláez', 49: 'Gallego', 50: 'Lizarazo', 51: 'Estrada', 52: 'Álvarez ', 53: 'Gallego', 54: 'Álzate Arteaga', 55: 'palacio', 56: 'Rojas', 57: 'Botero', 58: 'Rojas', 59: 'López', 60: 'Pascagaza', 61: 'Guanipa ', 62: 'torres', 63: 'Hincapié '}, 'email': {0: 'sergiosolano181@gmail.com', 1: 'salazaraguirrek1@gmail.com', 2: 'sebasesflorez@gmail.com', 3: 'ssofia.15mr@gmail.com', 4: 'ssofia.15mr@gmail.com', 5: 'cristiandhernandez687@gmail.com', 6: 'munozzara0@gmail.com', 7: 'moritaypineda12@gmail.com', 8: 'moritaypineda12@gmail.com', 9: 'ssofia.15mr@gmail.com', 10: 'juancamilozapata82@gmail.com', 11: 'andressolrzano67@gmail.com', 12: 'camilajaramejia0@gmail.com', 13: 'aleja2008.r@gmail.com', 14: 'cristinasaraza136@gmail.com', 15: 'camilajaramejia0@gmail.com', 16: 'qmanuela62@gmail.com', 17: 'juancamilozapata82@gmail.com', 18: 'camilajaramejia0@gmail.com', 19: 'camilajaramejia0@gmail.com', 20: 'sofiabedoya47@gmail.com', 21: 'laurasof.ren7@gmail.com', 22: 'camilalj0724@gmail.com', 23: 'nata.restrepo213@gmail.com', 24: 'solo123computador@gmail.com', 25: 'thomasvargas636@gmail.com', 26: 'sofiabedoya47@gmail.com', 27: 'luisfelipesuarez2007@gmail.com', 28: 'lopezsamlops23@gmail.com', 29: 'emilyramirezvelez123@gmail.com', 30: 'jeronimovilladaquintero@gmail.com', 31: 'mswbfamily@gmail.com', 32: 'johamportero1088@gmail.com', 33: 'jacoborendon2611@gmail.com', 34: 'cortes.isaza.luna@gmail.com', 35: 'santy3dc@gmail.com', 36: 'cortes.isaza.luna@gmail.com', 37: 'cortes.isaza.luna@gmail.com', 38: 'cortes.isaza.luna@gmail.com', 39: 'garciaarawen@gmail.com', 40: 'garciaarawen@gmail.com', 41: 'santiagoiemd@gmail.com', 42: 'anasofiaflorezgomez97@gmail.com', 43: 'guzmanordonezhector@gmail.com', 44: 'guzmanordonezhector@gmail.com', 45: 'samuelitocm123@gmail.com', 46: 'loscura156@gmail.com', 47: 'Castromguel3@gmail.com', 48: 'samuelarbelaezv@gmail.com', 49: 'sa0808170717@gmail.com', 50: 'dahianalizarazo401@gmail.com', 51: 'juanpabloestrada545@gmail.com', 52: 'felitaku25@gmail.com', 53: 'albergr2108@gmail.com', 54: 'thomasalzate710@gmail.com', 55: 'sanpalaciocar0705@gmail.com', 56: 'rojasvalentina0713@gmail.com', 57: 'jeanpoolboterolopez@gmail.com', 58: 'rojasvalentina0713@gmail.com', 59: 'dahianalopez650@gmail.com', 60: 'shjuanse17@gmail.com', 61: 'victoria.pgg.123@gmail.com', 62: 'torressarith04@gmail.com', 63: 'sofiso1204@gmail.com'}, 'celular': {0: 3218526746, 1: 3004040710, 2: 3103874631, 3: 3014605857, 4: 3014605857, 5: 3205450202, 6: 3233032131, 7: 3028348514, 8: 3028348514, 9: 3014605857, 10: 3219396931, 11: 3146729502, 12: 3025912530, 13: 3135686056, 14: 3155013217, 15: 3025912530, 16: 3106013587, 17: 3219396931, 18: 3025912530, 19: 3025912530, 20: 3136408861, 21: 3122926243, 22: 3136692871, 23: 3143962193, 24: 3233369220, 25: 3192085441, 26: 3136408861, 27: 3128304420, 28: 3229042622, 29: 3057592569, 30: 3127728240, 31: 3127416704, 32: 3126248747, 33: 3002514111, 34: 3046060082, 35: 3234277421, 36: 3046060082, 37: 3046060082, 38: 3046060082, 39: 3137160916, 40: 3137160916, 41: 3126504106, 42: 3206598144, 43: 3204126937, 44: 3204126937, 45: 3174858012, 46: 3218740602, 47: 3227136192, 48: 3028298274, 49: 3004701449, 50: 3126746030, 51: 3186776138, 52: 3233386775, 53: 3214325254, 54: 1089935811, 55: 3166701672, 56: 3218215247, 57: 3127702833, 58: 3218215247, 59: 3146100330, 60: 3165175712, 61: 3127732210, 62: 3156513243, 63: 3106328567}, 'pruebaId': {0: 245, 1: 247, 2: 248, 3: 250, 4: 250, 5: 252, 6: 254, 7: 255, 8: 446, 9: 447, 10: 280, 11: 286, 12: 293, 13: 297, 14: 298, 15: 302, 16: 307, 17: 451, 18: 460, 19: 462, 20: 313, 21: 318, 22: 383, 23: 384, 24: 386, 25: 388, 26: 461, 27: 456, 28: 463, 29: 468, 30: 469, 31: 243, 32: 244, 33: 251, 34: 249, 35: 253, 36: 453, 37: 457, 38: 458, 39: 295, 40: 306, 41: 301, 42: 303, 43: 316, 44: 316, 45: 317, 46: 325, 47: 368, 48: 369, 49: 372, 50: 377, 51: 381, 52: 382, 53: 385, 54: 387, 55: 380, 56: 394, 57: 396, 58: 449, 59: 444, 60: 445, 61: 448, 62: 450, 63: 459}, 'respuestas': {0: 73, 1: 123, 2: 112, 3: 170, 4: 108, 5: 71, 6: 15, 7: 98, 8: 182, 9: 166, 10: 12, 11: 163, 12: 22, 13: 67, 14: 140, 15: 54, 16: 89, 17: 182, 18: 34, 19: 181, 20: 47, 21: 8, 22: 11, 23: 62, 24: 74, 25: 30, 26: 182, 27: 182, 28: 80, 29: 182, 30: 182, 31: 180, 32: 149, 33: 108, 34: 91, 35: 55, 36: 50, 37: 50, 38: 182, 39: 31, 40: 166, 41: 170, 42: 95, 43: 14, 44: 15, 45: 75, 46: 98, 47: 178, 48: 133, 49: 69, 50: 44, 51: 47, 52: 42, 53: 60, 54: 55, 55: 30, 56: 14, 57: 16, 58: 182, 59: 182, 60: 182, 61: 182, 62: 182, 63: 182}, 'fechaPrueba': {0: Timestamp('2024-03-13 02:45:42'), 1: Timestamp('2024-03-13 02:47:04'), 2: Timestamp('2024-03-13 02:49:21'), 3: Timestamp('2024-03-13 02:46:03'), 4: Timestamp('2024-03-13 02:46:03'), 5: Timestamp('2024-03-13 02:49:42'), 6: Timestamp('2024-03-13 03:02:57'), 7: Timestamp('2024-03-13 02:57:08'), 8: Timestamp('2024-03-13 11:58:03'), 9: Timestamp('2024-03-13 12:13:48'), 10: Timestamp('2024-03-13 03:09:02'), 11: Timestamp('2024-03-13 03:30:42'), 12: Timestamp('2024-03-13 03:39:44'), 13: Timestamp('2024-03-13 03:47:02'), 14: Timestamp('2024-03-13 03:47:47'), 15: Timestamp('2024-03-13 03:48:09'), 16: Timestamp('2024-03-13 03:57:29'), 17: Timestamp('2024-03-13 13:28:48'), 18: Timestamp('2024-03-15 07:44:17'), 19: Timestamp('2024-03-15 07:53:38'), 20: Timestamp('2024-03-13 04:01:39'), 21: Timestamp('2024-03-13 04:13:51'), 22: Timestamp('2024-03-13 06:15:39'), 23: Timestamp('2024-03-13 06:14:14'), 24: Timestamp('2024-03-13 06:13:49'), 25: Timestamp('2024-03-13 06:15:08'), 26: Timestamp('2024-03-15 07:46:19'), 27: Timestamp('2024-03-14 10:38:37'), 28: Timestamp('2024-03-15 07:54:00'), 29: Timestamp('2024-03-17 07:19:46'), 30: Timestamp('2024-03-31 05:14:12'), 31: Timestamp('2024-03-13 02:31:17'), 32: Timestamp('2024-03-13 02:42:07'), 33: Timestamp('2024-03-13 02:47:18'), 34: Timestamp('2024-03-13 02:49:09'), 35: Timestamp('2024-03-13 02:55:14'), 36: Timestamp('2024-03-13 14:18:42'), 37: Timestamp('2024-03-14 15:13:11'), 38: Timestamp('2024-03-14 15:20:39'), 39: Timestamp('2024-03-13 03:43:48'), 40: Timestamp('2024-03-13 03:50:49'), 41: Timestamp('2024-03-13 03:50:59'), 42: Timestamp('2024-03-13 03:56:51'), 43: Timestamp('2024-03-13 04:05:40'), 44: Timestamp('2024-03-13 04:05:40'), 45: Timestamp('2024-03-13 04:05:27'), 46: Timestamp('2024-03-13 04:50:57'), 47: Timestamp('2024-03-13 06:00:16'), 48: Timestamp('2024-03-13 06:02:00'), 49: Timestamp('2024-03-13 06:07:39'), 50: Timestamp('2024-03-13 06:11:20'), 51: Timestamp('2024-03-13 06:12:46'), 52: Timestamp('2024-03-13 06:14:17'), 53: Timestamp('2024-03-13 06:13:58'), 54: Timestamp('2024-03-13 06:12:43'), 55: Timestamp('2024-03-13 06:16:55'), 56: Timestamp('2024-03-13 06:19:11'), 57: Timestamp('2024-03-13 06:22:11'), 58: Timestamp('2024-03-13 13:02:55'), 59: Timestamp('2024-03-13 09:06:47'), 60: Timestamp('2024-03-13 10:14:51'), 61: Timestamp('2024-03-13 12:35:54'), 62: Timestamp('2024-03-13 13:12:36'), 63: Timestamp('2024-03-15 07:44:13')}, 'fechaFinalizacion': {0: Timestamp('2024-03-13 03:04:03'), 1: Timestamp('2024-03-13 03:13:21'), 2: Timestamp('2024-03-13 03:13:04'), 3: Timestamp('2024-03-13 04:16:01'), 4: Timestamp('2024-03-13 04:16:01'), 5: Timestamp('2024-03-13 03:12:26'), 6: Timestamp('2024-03-13 03:05:11'), 7: Timestamp('2024-03-13 03:12:58'), 8: Timestamp('2024-03-13 12:52:40'), 9: Timestamp('2024-03-13 12:46:23'), 10: Timestamp('2024-03-13 03:12:34'), 11: Timestamp('2024-03-13 04:00:43'), 12: Timestamp('2024-03-13 03:43:28'), 13: Timestamp('2024-03-13 04:10:27'), 14: Timestamp('2024-03-13 04:12:51'), 15: Timestamp('2024-03-13 04:00:19'), 16: Timestamp('2024-03-13 04:14:54'), 17: Timestamp('2024-03-13 14:08:13'), 18: Timestamp('2024-03-15 07:51:41'), 19: Timestamp('2024-03-15 08:13:54'), 20: Timestamp('2024-03-13 04:13:14'), 21: Timestamp('2024-03-13 04:14:54'), 22: Timestamp('2024-03-13 06:24:37'), 23: Timestamp('2024-03-13 06:25:22'), 24: Timestamp('2024-03-13 06:28:21'), 25: Timestamp('2024-03-13 06:20:44'), 26: Timestamp('2024-03-15 08:10:38'), 27: Timestamp('2024-03-14 11:25:54'), 28: Timestamp('2024-03-15 08:08:44'), 29: Timestamp('2024-03-17 07:49:34'), 30: Timestamp('2024-03-31 05:45:47'), 31: Timestamp('2024-03-13 03:06:35'), 32: Timestamp('2024-03-13 03:12:22'), 33: Timestamp('2024-03-13 03:13:41'), 34: Timestamp('2024-03-13 03:05:36'), 35: Timestamp('2024-03-13 03:13:13'), 36: Timestamp('2024-03-13 14:22:57'), 37: Timestamp('2024-03-14 15:16:49'), 38: Timestamp('2024-03-14 15:37:57'), 39: Timestamp('2024-03-13 03:48:53'), 40: Timestamp('2024-03-13 04:11:06'), 41: Timestamp('2024-03-13 04:19:16'), 42: Timestamp('2024-03-13 04:14:40'), 43: Timestamp('2024-03-13 06:18:01'), 44: Timestamp('2024-03-13 06:18:01'), 45: Timestamp('2024-03-13 04:14:53'), 46: Timestamp('2024-03-13 05:53:01'), 47: Timestamp('2024-03-13 06:26:55'), 48: Timestamp('2024-03-13 06:26:10'), 49: Timestamp('2024-03-13 06:27:53'), 50: Timestamp('2024-03-13 06:28:34'), 51: Timestamp('2024-03-13 06:26:24'), 52: Timestamp('2024-03-13 06:26:05'), 53: Timestamp('2024-03-13 06:24:16'), 54: Timestamp('2024-03-13 06:27:29'), 55: Timestamp('2024-03-13 06:26:04'), 56: Timestamp('2024-03-13 06:24:16'), 57: Timestamp('2024-03-13 06:25:52'), 58: Timestamp('2024-03-13 13:52:46'), 59: Timestamp('2024-03-13 09:32:16'), 60: Timestamp('2024-03-13 10:52:18'), 61: Timestamp('2024-03-13 13:05:27'), 62: Timestamp('2024-03-13 13:33:13'), 63: Timestamp('2024-03-15 08:13:43')}, 'tiempo': {0: 18, 1: 26, 2: 24, 3: 90, 4: 90, 5: 23, 6: 2, 7: 16, 8: 55, 9: 33, 10: 4, 11: 30, 12: 4, 13: 23, 14: 25, 15: 12, 16: 17, 17: 39, 18: 7, 19: 20, 20: 12, 21: 1, 22: 9, 23: 11, 24: 15, 25: 6, 26: 24, 27: 47, 28: 15, 29: 30, 30: 32, 31: 35, 32: 30, 33: 26, 34: 16, 35: 18, 36: 4, 37: 4, 38: 17, 39: 5, 40: 20, 41: 28, 42: 18, 43: 132, 44: 132, 45: 9, 46: 62, 47: 27, 48: 24, 49: 20, 50: 17, 51: 14, 52: 12, 53: 10, 54: 15, 55: 9, 56: 5, 57: 4, 58: 50, 59: 25, 60: 37, 61: 30, 62: 21, 63: 30}, 'primerArea': {0: 'Arte y diseño', 1: 'Ciencias de la salud', 2: 'Ciencias sociales y humanidades', 3: 'Ingenierías y tecnología', 4: 'Ingenierías y tecnología', 5: 'Ciencias administrativas y económicas', 6: 'Arte y diseño', 7: 'Ingenierías y tecnología', 8: 'Ingenierías y tecnología', 9: 'Ingenierías y tecnología', 10: 'Ciencias exactas y naturales', 11: 'Ciencias de la salud', 12: 'Arte y diseño', 13: 'Ciencias de la salud', 14: 'Ciencias de la salud', 15: 'Ingenierías y tecnología', 16: 'Ingenierías y tecnología', 17: 'Arte y diseño', 18: 'Ciencias exactas y naturales', 19: 'Ciencias sociales y humanidades', 20: 'Ciencias sociales y humanidades', 21: 'Ingenierías y tecnología', 22: 'Ciencias exactas y naturales', 23: 'Ingenierías y tecnología', 24: 'Ciencias sociales y humanidades', 25: 'Ciencias sociales y humanidades', 26: 'Ciencias sociales y humanidades', 27: 'Ingenierías y tecnología', 28: 'Ciencias de la salud', 29: 'Ingenierías y tecnología', 30: 'Ingenierías y tecnología', 31: 'Ingenierías y tecnología', 32: 'Ciencias exactas y naturales', 33: 'Ciencias exactas y naturales', 34: 'Ciencias de la salud', 35: 'Ingenierías y tecnología', 36: 'Ingenierías y tecnología', 37: 'Ciencias de la salud', 38: 'Ingenierías y tecnología', 39: 'Ciencias sociales y humanidades', 40: 'Ciencias sociales y humanidades', 41: 'Ingenierías y tecnología', 42: 'Ciencias de la salud', 43: 'Ciencias administrativas y económicas', 44: 'Ciencias administrativas y económicas', 45: 'Ciencias sociales y humanidades', 46: 'Arte y diseño', 47: 'Ingenierías y tecnología', 48: 'Arte y diseño', 49: 'Ingenierías y tecnología', 50: 'Ingenierías y tecnología', 51: 'Ingenierías y tecnología', 52: 'Ciencias sociales y humanidades', 53: 'Ingenierías y tecnología', 54: 'Arte y diseño', 55: 'Ciencias sociales y humanidades', 56: 'Ciencias de la salud', 57: 'Ciencias administrativas y económicas', 58: 'Ciencias de la salud', 59: 'Ciencias sociales y humanidades', 60: 'Ciencias de la salud', 61: 'Ingenierías y tecnología', 62: 'Ciencias sociales y humanidades', 63: 'Ciencias sociales y humanidades'}, 'segundaArea': {0: 'Ciencias sociales y humanidades', 1: 'Ciencias sociales y humanidades', 2: 'Ciencias de la salud', 3: 'Ciencias exactas y naturales', 4: 'Ciencias exactas y naturales', 5: 'Ciencias exactas y naturales', 6: 'Ciencias sociales y humanidades', 7: 'Ciencias administrativas y económicas', 8: 'Ciencias exactas y naturales', 9: 'Ciencias exactas y naturales', 10: 'Ingenierías y tecnología', 11: 'Ingenierías y tecnología', 12: 'Ciencias de la salud', 13: 'Ciencias administrativas y económicas', 14: 'Ingenierías y tecnología', 15: 'Arte y diseño', 16: 'Ciencias de la salud', 17: 'Ingenierías y tecnología', 18: 'Ciencias sociales y humanidades', 19: 'Ciencias de la salud', 20: 'Ingenierías y tecnología', 21: 'Ciencias exactas y naturales', 22: 'Ciencias sociales y humanidades', 23: 'Arte y diseño', 24: 'Ciencias de la salud', 25: 'Arte y diseño', 26: 'Ciencias de la salud', 27: 'Ciencias exactas y naturales', 28: 'Ingenierías y tecnología', 29: 'Ciencias exactas y naturales', 30: 'Ciencias exactas y naturales', 31: 'Ciencias exactas y naturales', 32: 'Arte y diseño', 33: 'Ingenierías y tecnología', 34: 'Ciencias exactas y naturales', 35: 'Ciencias de la salud', 36: 'Ciencias de la salud', 37: 'Ingenierías y tecnología', 38: 'Ciencias exactas y naturales', 39: 'Ingenierías y tecnología', 40: 'Ciencias de la salud', 41: 'Ciencias exactas y naturales', 42: 'Ciencias sociales y humanidades', 43: 'Arte y diseño', 44: 'Arte y diseño', 45: 'Arte y diseño', 46: 'Ingenierías y tecnología', 47: 'Ciencias exactas y naturales', 48: 'Ciencias sociales y humanidades', 49: 'Ciencias exactas y naturales', 50: 'Ciencias administrativas y económicas', 51: 'Ciencias exactas y naturales', 52: 'Arte y diseño', 53: 'Ciencias exactas y naturales', 54: 'Ciencias exactas y naturales', 55: 'Ingenierías y tecnología', 56: 'Ciencias sociales y humanidades', 57: 'Ingenierías y tecnología', 58: 'Ciencias sociales y humanidades', 59: 'Ingenierías y tecnología', 60: 'Ingenierías y tecnología', 61: 'Ciencias sociales y humanidades', 62: 'Ingenierías y tecnología', 63: 'Arte y diseño'}, 'tercerArea': {0: 'Ciencias exactas y naturales', 1: 'Ciencias administrativas y económicas', 2: 'Ciencias administrativas y económicas', 3: 'Ciencias exactas y naturales', 4: 'Arte y diseño', 5: 'Ingenierías y tecnología', 6: 'Ciencias exactas y naturales', 7: 'Ciencias sociales y humanidades', 8: 'Ciencias sociales y humanidades', 9: 'Ciencias de la salud', 10: 'Ciencias de la salud', 11: 'Ciencias exactas y naturales', 12: 'Ciencias exactas y naturales', 13: 'Ingenierías y tecnología', 14: 'Ciencias sociales y humanidades', 15: 'Ciencias de la salud', 16: 'Ciencias sociales y humanidades', 17: 'Ciencias exactas y naturales', 18: 'Ciencias de la salud', 19: 'Ciencias exactas y naturales', 20: 'Ciencias de la salud', 21: 'Ciencias sociales y humanidades', 22: 'Ciencias administrativas y económicas', 23: 'Ciencias de la salud', 24: 'Arte y diseño', 25: 'Ciencias de la salud', 26: 'Ingenierías y tecnología', 27: 'Ciencias de la salud', 28: 'Ciencias sociales y humanidades', 29: 'Ciencias de la salud', 30: 'Ciencias sociales y humanidades', 31: 'Ciencias de la salud', 32: 'Ciencias administrativas y económicas', 33: 'Ciencias sociales y humanidades', 34: 'Ingenierías y tecnología', 35: 'Ciencias administrativas y económicas', 36: 'Ciencias exactas y naturales', 37: 'Ciencias exactas y naturales', 38: 'Ciencias de la salud', 39: 'Ciencias de la salud', 40: 'Arte y diseño', 41: 'Arte y diseño', 42: 'Arte y diseño', 43: 'Ciencias sociales y humanidades', 44: 'Ciencias sociales y humanidades', 45: 'Ciencias exactas y naturales', 46: 'Ciencias sociales y humanidades', 47: 'Ciencias de la salud', 48: 'Ingenierías y tecnología', 49: 'Ciencias administrativas y económicas', 50: 'Ciencias exactas y naturales', 51: 'Ciencias de la salud', 52: 'Ingenierías y tecnología', 53: 'Ciencias de la salud', 54: 'Ingenierías y tecnología', 55: 'Ciencias de la salud', 56: 'Ciencias exactas y naturales', 57: 'Ciencias sociales y humanidades', 58: 'Ciencias administrativas y económicas', 59: 'Arte y diseño', 60: 'Arte y diseño', 61: 'Arte y diseño', 62: 'Ciencias de la salud', 63: 'Ciencias de la salud'}, 'personalidad': {0: 'Creativo innovador, No convencional, Extrovertido, Detallista, Importancia estética', 1: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 2: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 3: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 4: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 5: 'Sociable, Emprendedor iniciativa, Narcisista autosuficiente, Dominante', 6: 'Creativo innovador, No convencional, Extrovertido, Detallista, Importancia estética', 7: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 8: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 9: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 10: 'Investigador disciplinado, Curioso, Paciente, Introvertido', 11: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 12: 'Creativo innovador, No convencional, Extrovertido, Detallista, Importancia estética', 13: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 14: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 15: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 16: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 17: 'Creativo innovador, No convencional, Extrovertido, Detallista, Importancia estética', 18: 'Investigador disciplinado, Curioso, Paciente, Introvertido', 19: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 20: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 21: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 22: 'Investigador disciplinado, Curioso, Paciente, Introvertido', 23: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 24: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 25: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 26: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 27: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 28: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 29: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 30: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 31: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 32: 'Investigador disciplinado, Curioso, Paciente, Introvertido', 33: 'Investigador disciplinado, Curioso, Paciente, Introvertido', 34: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 35: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 36: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 37: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 38: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 39: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 40: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 41: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 42: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 43: 'Sociable, Emprendedor iniciativa, Narcisista autosuficiente, Dominante', 44: 'Sociable, Emprendedor iniciativa, Narcisista autosuficiente, Dominante', 45: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 46: 'Creativo innovador, No convencional, Extrovertido, Detallista, Importancia estética', 47: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 48: 'Creativo innovador, No convencional, Extrovertido, Detallista, Importancia estética', 49: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 50: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 51: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 52: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 53: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 54: 'Creativo innovador, No convencional, Extrovertido, Detallista, Importancia estética', 55: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 56: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 57: 'Sociable, Emprendedor iniciativa, Narcisista autosuficiente, Dominante', 58: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 59: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 60: 'Consciente ayudador, Narcisista autosuficiente, Realista practico, Sociable', 61: 'Realista practico, Narcisista autosuficiente, Convencional, Introvertido', 62: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador', 63: 'Soñador idealista, Observador, Consciente ayudador, Introvertido, Analizador'}, 'gustos': {0: 'Aire libre, Ideas nuevas, Cine arte, Museos, Cultura, Teatro, Apreciación estética', 1: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 2: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 3: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 4: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 5: 'Dinero, Lujos, Estatus, Amistades', 6: 'Aire libre, Ideas nuevas, Cine arte, Museos, Cultura, Teatro, Apreciación estética', 7: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 8: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 9: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 10: 'Laboratorios, Números, Como funcionan las cosas, Investigación, Naturaleza', 11: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 12: 'Aire libre, Ideas nuevas, Cine arte, Museos, Cultura, Teatro, Apreciación estética', 13: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 14: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 15: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 16: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 17: 'Aire libre, Ideas nuevas, Cine arte, Museos, Cultura, Teatro, Apreciación estética', 18: 'Laboratorios, Números, Como funcionan las cosas, Investigación, Naturaleza', 19: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 20: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 21: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 22: 'Laboratorios, Números, Como funcionan las cosas, Investigación, Naturaleza', 23: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 24: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 25: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 26: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 27: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 28: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 29: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 30: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 31: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 32: 'Laboratorios, Números, Como funcionan las cosas, Investigación, Naturaleza', 33: 'Laboratorios, Números, Como funcionan las cosas, Investigación, Naturaleza', 34: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 35: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 36: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 37: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 38: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 39: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 40: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 41: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 42: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 43: 'Dinero, Lujos, Estatus, Amistades', 44: 'Dinero, Lujos, Estatus, Amistades', 45: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 46: 'Aire libre, Ideas nuevas, Cine arte, Museos, Cultura, Teatro, Apreciación estética', 47: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 48: 'Aire libre, Ideas nuevas, Cine arte, Museos, Cultura, Teatro, Apreciación estética', 49: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 50: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 51: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 52: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 53: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 54: 'Aire libre, Ideas nuevas, Cine arte, Museos, Cultura, Teatro, Apreciación estética', 55: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 56: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 57: 'Dinero, Lujos, Estatus, Amistades', 58: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 59: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 60: 'Cuerpo humano, Concepto de la vida y sus procesos, Nutricional, Investigación', 61: 'Avances TIC gadgets, Funcionamiento de las cosas, Innovación, Video Juegos, Maquinas', 62: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo', 63: 'Lectura, Difusión de la cultura, Relaciones personales, Servicio a la comunidad, Gusto por el cambio, Fenómenos sociales, Trabajo de campo'}, 'habilidades': {0: 'Perceptivo y manual, Razonamiento abstracción, Comunicación social, Destreza manual, Sensibilidad artística y cultural, Creatividad', 1: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 2: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 3: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 4: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 5: 'Capacidad lingüística, Razonamiento numérico, Razonamiento abstracción, Organización planificación', 6: 'Perceptivo y manual, Razonamiento abstracción, Comunicación social, Destreza manual, Sensibilidad artística y cultural, Creatividad', 7: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 8: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 9: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 10: 'Organización planificación, Observación y análisis, Abstracción, Trabajo en equipo, Método científico, Sentido de cooperación', 11: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 12: 'Perceptivo y manual, Razonamiento abstracción, Comunicación social, Destreza manual, Sensibilidad artística y cultural, Creatividad', 13: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 14: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 15: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 16: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 17: 'Perceptivo y manual, Razonamiento abstracción, Comunicación social, Destreza manual, Sensibilidad artística y cultural, Creatividad', 18: 'Organización planificación, Observación y análisis, Abstracción, Trabajo en equipo, Método científico, Sentido de cooperación', 19: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 20: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 21: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 22: 'Organización planificación, Observación y análisis, Abstracción, Trabajo en equipo, Método científico, Sentido de cooperación', 23: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 24: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 25: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 26: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 27: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 28: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 29: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 30: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 31: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 32: 'Organización planificación, Observación y análisis, Abstracción, Trabajo en equipo, Método científico, Sentido de cooperación', 33: 'Organización planificación, Observación y análisis, Abstracción, Trabajo en equipo, Método científico, Sentido de cooperación', 34: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 35: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 36: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 37: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 38: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 39: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 40: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 41: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 42: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 43: 'Capacidad lingüística, Razonamiento numérico, Razonamiento abstracción, Organización planificación', 44: 'Capacidad lingüística, Razonamiento numérico, Razonamiento abstracción, Organización planificación', 45: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 46: 'Perceptivo y manual, Razonamiento abstracción, Comunicación social, Destreza manual, Sensibilidad artística y cultural, Creatividad', 47: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 48: 'Perceptivo y manual, Razonamiento abstracción, Comunicación social, Destreza manual, Sensibilidad artística y cultural, Creatividad', 49: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 50: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 51: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 52: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 53: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 54: 'Perceptivo y manual, Razonamiento abstracción, Comunicación social, Destreza manual, Sensibilidad artística y cultural, Creatividad', 55: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 56: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 57: 'Capacidad lingüística, Razonamiento numérico, Razonamiento abstracción, Organización planificación', 58: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 59: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 60: 'Organización planificación, Razonamiento abstracción, Memoria, Observación y análisis, Método científico', 61: 'Organización planificación, Observación y análisis, Razonamiento abstracción, Razonamiento numérico', 62: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico', 63: 'Analizador, Capacidad lingüística, Razonamiento abstracción, Análisis y síntesis, Adaptación al cambio, Responsabilidad social, Pensamiento critico'}, 'carreras': {0: 'Arquitectura, Cine y televisión, Diseño y gestión de moda, Gastronomía, Diseño gráfico, Artes escénicas, Historia y Literatura', 1: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 2: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 3: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 4: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 5: 'Contaduría Publica, Negocios Internacionales, Administración de empresas, Hotelería y Turismo, Contabilidad y finanzas', 6: 'Arquitectura, Cine y televisión, Diseño y gestión de moda, Gastronomía, Diseño gráfico, Artes escénicas, Historia y Literatura', 7: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 8: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 9: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 10: 'Bioingeniería, Bacteriología, Biología, Ecología, Física y Química, Matemáticas', 11: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 12: 'Arquitectura, Cine y televisión, Diseño y gestión de moda, Gastronomía, Diseño gráfico, Artes escénicas, Historia y Literatura', 13: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 14: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 15: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 16: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 17: 'Arquitectura, Cine y televisión, Diseño y gestión de moda, Gastronomía, Diseño gráfico, Artes escénicas, Historia y Literatura', 18: 'Bioingeniería, Bacteriología, Biología, Ecología, Física y Química, Matemáticas', 19: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 20: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 21: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 22: 'Bioingeniería, Bacteriología, Biología, Ecología, Física y Química, Matemáticas', 23: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 24: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 25: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 26: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 27: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 28: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 29: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 30: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 31: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 32: 'Bioingeniería, Bacteriología, Biología, Ecología, Física y Química, Matemáticas', 33: 'Bioingeniería, Bacteriología, Biología, Ecología, Física y Química, Matemáticas', 34: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 35: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 36: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 37: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 38: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 39: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 40: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 41: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 42: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 43: 'Contaduría Publica, Negocios Internacionales, Administración de empresas, Hotelería y Turismo, Contabilidad y finanzas', 44: 'Contaduría Publica, Negocios Internacionales, Administración de empresas, Hotelería y Turismo, Contabilidad y finanzas', 45: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 46: 'Arquitectura, Cine y televisión, Diseño y gestión de moda, Gastronomía, Diseño gráfico, Artes escénicas, Historia y Literatura', 47: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 48: 'Arquitectura, Cine y televisión, Diseño y gestión de moda, Gastronomía, Diseño gráfico, Artes escénicas, Historia y Literatura', 49: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 50: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 51: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 52: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 53: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 54: 'Arquitectura, Cine y televisión, Diseño y gestión de moda, Gastronomía, Diseño gráfico, Artes escénicas, Historia y Literatura', 55: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 56: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 57: 'Contaduría Publica, Negocios Internacionales, Administración de empresas, Hotelería y Turismo, Contabilidad y finanzas', 58: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 59: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 60: 'Medicina, Enfermería, Terapeuta ocupacional, Fisioterapia, Nutrición y Dieta.', 61: 'Ing. Industrial, Ing. en Telecomunicaciones, Ing. Mecatrónica, Tecnologías en desarrollo de Software, Ing. de Sistemas, Ing. Electrónica, Ing. Civil', 62: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social', 63: 'Licenciatura en Filosofía, Licenciatura en Lenguas Extranjeras, Teología, Derecho, Ciencia Política, Comunicación social, Psicología, Trabajo social'}}
  df=pd.DataFrame(di)
  df=df.groupby('documento', group_keys=False, as_index=True).apply(lambda x: x.loc[x.respuestas.idxmax()])
  cols_li=list(df.columns[-4:])
  for c in cols_li:
      df[c]=df[c].str.split(', ')
  return df

df=data()

i=st.selectbox('Identificación',options=df.index.to_list())

nombre=df.loc[i]['nombre'].capitalize()
apellido=df.loc[i]['apellido'].capitalize()
fecha=df.loc[i]['fechaPrueba']
fecha=fecha.strftime(r'%d de marzo de %Y')
tiempo=df.loc[i]['tiempo']
respuestas=df.loc[i]['respuestas']
documento=df.loc[i]['documento']
celular=df.loc[i]['celular']
correo=df.loc[i]['email']
primerArea=df.loc[i]['primerArea']
segundaArea=df.loc[i]['segundaArea']
tercerArea=df.loc[i]['tercerArea']

carreras=''
for j in df.loc[i]['carreras']:
   carreras=carreras+f'<li><small>{j}</small></li>'

personalidad=''
for k in df.loc[i]['personalidad']:
   personalidad=personalidad+f'<li><svg viewbox="0 0 100 100"><circle class="cbar" cx="50" cy="50" r="45"></circle></svg><span>{k}</span></li>'

habilidades=''
for l in df.loc[i]['habilidades']:
   habilidades=habilidades+f'<div class="art"><i class="{habilidades_iconos[l]}"></i><span>{l}</span></div>'

gustos=''
for m in df.loc[i]['gustos']:
   gustos=gustos+f'<div class="art"><i class="{gustos_iconos[m]}"></i><span>{m}</span></div>'


html_t=f'''
<html>
<head>
  <meta charset="UTF-8">
  <title>Informe Orientación Profesional</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://kit.fontawesome.com/9d3192fc0a.js" crossorigin="anonymous"></script>
<style>
    @import url("https://fonts.googleapis.com/css?family=Montserrat");
* {{
  outline: none;
}}

*,
*:before,
*:after {{
  box-sizing: inherit;
}}

html,
body {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  transition: 0.5s;
  background: #ffffff;
  cursor: default;
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
}}

a {{
  text-decoration: none;
  color: #ffffff;
  display: block;
  transition-duration: 0.3s;
  line-height: 20px;
}}

ul {{
  list-style-type: none;
  padding: 0;
}}

h3 {{
  color: #ffb300;
  margin: 10px 0;
  font-size: 1.25em;
}}

h2 {{
  color: #ffb300;
  margin: 10px 0;
  font-size: 14px;
}}

.resume {{
  width: 960px;
  background: #1a237e;
  color: #ffffff;
  margin: 20px auto;
  box-shadow: 10px 10px #0e1442;
  position: relative;
  display: flex;
}}

.resume .base,
.resume .func {{
  box-sizing: border-box;
  float: left;
}}

.resume .base > div,
.resume .func > div {{
  padding-bottom: 10px;
}}

.resume .base > div:last-of-type,
.resume .func > div:last-of-type {{
  padding-bottom: 0;
}}

.resume .base {{
  width: 30%;
  padding: 30px 15px;
  background: #283593;
  color: #ffffff;
}}

.resume .base .profile {{
  background: #ffb300;
  padding: 30px 15px 40px 15px;
  margin: -30px -15px 45px -15px;
  position: relative;
  z-index: 2;
}}

.resume .base .profile::after {{
  content: "";
  position: absolute;
  background: #303f9f;
  width: 100%;
  height: 30px;
  bottom: -15px;
  left: 0;
  transform: skewY(-5deg);
  z-index: -1;
}}

.resume .base .profile .photo img {{
  width: 100%;
  border-radius: 50%;
}}

.resume .base .profile .photo {{
  display: flex;
  justify-content: center;
  align-items: center;
}}

.resume .base .profile .fa-rocket {{
  font-size: 100px;
  text-align: center;
  margin: auto;
  color: #283593;
}}

.resume .base .profile .info {{
  text-align: center;
  color: #ffffff;
}}

.resume .base .profile .info .name {{
  margin-top: 10px;
  margin-bottom: 0;
  font-size: 1.75em;
  color: #1a237e;
}}

.resume .base .profile .info .job {{
  margin-top: 10px;
  margin-bottom: 0;
  font-size: 1em;
  color: #283593;
}}

.resume .base .contact div {{
  line-height: 28px;
}}

.resume .base .contact .email span {{
  font-size: 10px;
}}

.resume .base .contact div a:hover {{
  color: #fdd835;
}}

.resume .base .contact div a:hover span::after {{
  width: 100%;
}}

.resume .base .contact div:hover i {{
  color: #fdd835;
}}

.resume .base .contact div i {{
  color: #ffb300;
  width: 20px;
  height: 20px;
  font-size: 20px;
  text-align: center;
  margin-right: 15px;
  transition-duration: 0.3s;
}}

.resume .base .contact div span {{
  position: relative;
}}

.resume .base .contact div span::after {{
  content: "";
  position: absolute;
  background: #fdd835;
  height: 1px;
  width: 0;
  bottom: 0;
  left: 0;
  transition-duration: 0.3s;
}}

.resume .base .about i {{
  color: #ffb300;
  width: 20px;
  height: 20px;
  font-size: 20px;
  text-align: center;
  margin-right: 15px;
  transition-duration: 0.3s;
}}

.resume .func {{
  width: 75%;
  padding: 30px;
}}

.resume .func:hover > div {{
  transition-duration: 0.5s;
}}

.resume .func:hover > div:hover h3 i {{
  transform: scale(1.25);
}}

.resume .func:hover > div:not(:hover) {{
  opacity: 0.5;
}}

.resume .func h3 {{
  transition-duration: 0.3s;
  margin-top: 0;
}}

.resume .func h3 i {{
  color: #283593;
  background: #ffb300;
  width: 42px;
  height: 42px;
  font-size: 20px;
  line-height: 42px;
  border-radius: 50%;
  text-align: center;
  vertical-align: middle;
  margin-right: 8px;
  transition-duration: 0.3s;
}}

.resume .func .work,
.resume .func .edu {{
  float: left;
}}

.resume .func .work small,
.resume .func .edu small {{
  display: block;
  opacity: 0.7;
}}

.resume .func .work ul li,
.resume .func .edu ul li {{
  position: relative;
  margin-left: 15px;
  padding-left: 25px;
  padding-bottom: 15px;
}}

.resume .func .work ul li:hover::before,
.resume .func .edu ul li:hover::before {{
  -webkit-animation: circle 1.2s infinite;
          animation: circle 1.2s infinite;
}}

.resume .func .work ul li:hover span,
.resume .func .edu ul li:hover span {{
  color: #fdd835;
}}

@-webkit-keyframes circle {{
  from {{
    box-shadow: 0 0 0 0px #fdd835;
  }}
  to {{
    box-shadow: 0 0 0 6px rgba(255, 255, 255, 0);
  }}
}}

@keyframes circle {{
  from {{
    box-shadow: 0 0 0 0px #fdd835;
  }}
  to {{
    box-shadow: 0 0 0 6px rgba(255, 255, 255, 0);
  }}
}}
.resume .func .work ul li:first-of-type::before,
.resume .func .edu ul li:first-of-type::before {{
  width: 10px;
  height: 10px;
  left: 1px;
  vertical-align: middle;
}}

.resume .func .work ul li:last-of-type,
.resume .func .edu ul li:last-of-type {{
  padding-bottom: 3px;
  vertical-align: middle;
}}

.resume .func .work ul li:last-of-type::after,
.resume .func .edu ul li:last-of-type::after {{
  border-radius: 1.5px;
  vertical-align: middle;
}}

.resume .func .work ul li::before,
.resume .func .work ul li::after,
.resume .func .edu ul li::before,
.resume .func .edu ul li::after {{
  content: "";
  display: block;
  position: absolute;
}}

.resume .func .work ul li::before,
.resume .func .edu ul li::before {{
  width: 7px;
  height: 7px;
  border: 3px solid #ffffff;
  background: #ffb300;
  border-radius: 50%;
  left: 3px;
  z-index: 1;
  vertical-align: middle;
}}

.resume .func .work ul li::after,
.resume .func .edu ul li::after {{
  width: 3px;
  height: 100%;
  background: #ffffff;
  left: 5px;
  top: 0;
}}

.resume .func .work ul li span,
.resume .func .edu ul li span {{
  transition-duration: 0.3s;
  vertical-align: middle;
}}

.resume .func .work {{
  width: 40%;
  height: 32%;
  background: #283593;
  padding: 15px;
  margin: 0 4% 15px 0;
  vertical-align: middle;
}}

.resume .func .edu {{
  width: 56%;
  height: 32%;
  background: #283593;
  padding: 15px;
  vertical-align: middle;
}}

.resume .func .skills-prog {{
  clear: both;
  background: #283593;
  padding: 15px;
}}

.resume .func .skills-prog ul {{
  margin-left: 15px;
}}

.resume .func .skills-prog ul li {{
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  transition-duration: 0.3s;
}}

.resume .func .skills-prog ul li:hover {{
  color: #fdd835;
}}

.resume .func .skills-prog ul li:hover .skills-bar .bar {{
  background: #fdd835;
  box-shadow: 0 0 0 1px #fdd835;
}}

.resume .func .skills-prog ul li span {{
  display: block;
  width: 120px;
}}

.resume .func .skills-prog ul li .skills-bar {{
  background: #ffffff;
  height: 2px;
  width: calc(100% - 120px);
  position: relative;
  border-radius: 2px;
}}

.resume .func .skills-prog ul li .skills-bar .bar {{
  position: absolute;
  top: -1px;
  height: 4px;
  background: #ffb300;
  box-shadow: 0 0 0 #ffb300;
  border-radius: 5px;
}}

.resume .func .skills-soft {{
  clear: both;
  background: #283593;
  padding: 15px;
  margin: 15px 0 0;
}}

.resume .func .skills-soft ul {{
  display: flex;
  justify-content: space-between;
  text-align: center;
  font-size: 12px;
}}

.resume .func .skills-soft ul li {{
  position: relative;
}}

.resume .func .skills-soft ul li:hover svg .cbar {{
  stroke: #fdd835;
  stroke-width: 4px;
}}

.resume .func .skills-soft ul li:hover span,
.resume .func .skills-soft ul li:hover small {{
  transform: scale(1.2);
}}

.resume .func .skills-soft ul li svg {{
  width: 90%;
  fill: transparent;
}}

.resume .func .skills-soft ul li svg circle {{
  stroke-width: 1px;
  stroke: #ffffff;
}}

.resume .func .skills-soft ul li svg .cbar {{
  stroke-width: 3px;
  stroke: #ffb300;
  stroke-linecap: round;
}}

.resume .func .skills-soft ul li span,
.resume .func .skills-soft ul li small {{
  position: absolute;
  display: block;
  width: 70%;
  top: 80%;
  transition-duration: 0.3s;
}}

.resume .func .skills-soft ul li span {{
  top: 38%;
  left: 15%;
}}

.resume .func .interests {{
  background: #283593;
  margin: 15px 0 0;
  padding: 15px;
  
}}

.resume .func .interests-items {{
  box-sizing: border-box;
  padding: 0 0 15px;
  width: 100%;
  text-align: center;
  display: flex;
  justify-content: space-between;
}}

.resume .func .interests-items div {{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100px;
  height: 100px;
  border-radius: 50%;
}}

.resume .func .interests-items div:hover i {{
  transform: scale(1.2);
}}

.resume .func .interests-items div:hover span {{
  color: #fdd835;
  transition-duration: 0.3s;
}}

.resume .func .interests-items div i {{
  font-size: 45px;
  width: 60px;
  height: 60px;
  line-height: 60px;
  color: #ffb300;
  transition-duration: 0.3s;
}}

.resume .func .interests-items div span {{
  font-size: 12px;
  display: block;
}}
</style>
</head>
<body>
<!-- partial:index.partial.html -->
<div class="resume">
  <div class="base">
    <div class="profile">
      <div class="photo">
        <!--<img src="" /> -->
        <i class="fas fa-rocket"></i>
      </div>
      <div class="info">
        <h1 class="name"> {nombre} {apellido}</h1>
        <h2 class="job">Resultados Prueba de Orientación Profesional</h2>
      </div>
    </div>
    <div class="about">
      <h3>Datos de Prueba</h3>
        <a>Fecha: {fecha}</a>
        <a>Duración: {tiempo} minutos</a>
        <a>Respuestas a {respuestas} preguntas</a>
    </div>
    <div class="contact">
      <h3>Datos del estudiante</h3>
      <div class="call"><i class="fa-solid fa-id-card"></i><span>{documento}</span></a></div>
      <div class="call"><i class="fas fa-mobile-alt"></i><span>{celular}</span></a></div>
      <div class="address"><i class="fas fa-map-marker"></i><span>I.E. María Dolorosa</span></a></div>
      <div class="email"><i class="fas fa-envelope"></i><span>{correo}</span></a></div>
    </div>
    <div class="about">
      <h2>Prueba realizada por:</h2>
      <i class="fa-solid fa-school"></i>
        <a>Fundación Universitaria del Área Andina</a>
      <h2>Informe realizado por:</h2>
      <i class="fa-solid fa-person-chalkboard"></i>
      
        <a>Angela Rodas Panesso</a>
        <small>Docente Orientadora <br> I.E. María Dolorosa</small>
    </div>
  </div>
  <div class="func">

    
    <div class="work">
      <h3><i class="fas fa-university"></i>Areas</h3>
      <ul>
        <li><span>Primera</span><small>{primerArea}</small></li>
        <li><span>Segunda</span><small>{segundaArea}</small></li>
        <li><span>Tercera</span><small>{tercerArea}</small></li>
      </ul>
    </div>
    <div class="edu">
      <h3><i class="fa fa-graduation-cap"></i>Carreras</h3>
      <ul>
        {carreras}
      </ul>
    </div>
    <div class="skills-soft">
      <h3><i class="fas fa-user"></i>Personalidad</h3>
      <ul>
        {personalidad}
      </ul>
    </div>
    <div class="interests">
      <h3><i class="fas fa-thumbs-up"></i>Habilidades</h3>
      <div class="interests-items">
        {habilidades}
      </div>
    </div>
    <div class="interests">
      <h3><i class="fas fa-star"></i>Gustos</h3>
      <div class="interests-items">
        {gustos}
      </div>
    </div>
  </div>
</div>
</body>
</html>
'''

components.html(html_t, height=1200, width=1000, scrolling=True)
