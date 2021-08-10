import streamlit as st
import streamlit.components.v1 as components

def tableau():
    html_temp = """<div class='tableauPlaceholder' id='viz1622585930212' style='position: relative'><noscript><a href='#'><img alt='Historia 1 ' 
    src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Hi&#47;HistoriadelamortalidadenEspaaentre1980y2019&#47;Historia1&#47;1_rss.png' 
    style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
    <param name='embed_code_version' value='3' /> 
    <param name='site_root' value='' />
    <param name='name' value='HistoriadelamortalidadenEspaaentre1980y2019&#47;Historia1' />
    <param name='tabs' value='no' />
    <param name='toolbar' value='yes' />
    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Hi&#47;HistoriadelamortalidadenEspaaentre1980y2019&#47;Historia1&#47;1.png' /> 
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='language' value='es-ES' /></object></div>                
    <script type='text/javascript'>                    
    var divElement = document.getElementById('viz1622585930212');                    
    var vizElement = divElement.getElementsByTagName('object')[0];                    
    vizElement.style.width='1016px';
    vizElement.style.height='991px';                    
    var scriptElement = document.createElement('script');                    
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
    vizElement.parentNode.insertBefore(scriptElement, vizElement);                
    </script>"""

    components.html(html_temp, width=1130, height=700)
    max_width_str = f"max-width: 1030px;"
    st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)


