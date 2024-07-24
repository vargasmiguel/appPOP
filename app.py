import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

st.set_page_config(layout='wide',
                           page_title="Informe Orientación Profesional",
                           page_icon="📗")

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
  df=pd.read_excel('Datos_otog.xlsx')
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
