import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Página de Vendas Exclusiva",
    page_icon="🚀",
    layout="wide", # Layout wide para melhor aproveitamento de tela em desktops
    initial_sidebar_state="collapsed"
)

# --- Estilo (Streamlit nativo é limpo e moderno, mas podemos adicionar um toque) ---
# O Streamlit é responsivo por padrão. O layout="wide" ajuda em telas maiores.
# Usarei containers e colunas para um design mais estruturado.

# --- 1. Título Chamativo ---
st.title("🚀 **Domine suas finanças: O Guia Definitivo para Aplicações no seu dia a dia**")
st.subheader("Transforme seus ganhos em aplicações para seu futuro!")
st.markdown("---")

# --- 2. Descrição do Produto/Serviço ---
st.header("O Que Você Vai Aprender:")

# Usando colunas para um layout mais agradável
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    Este e-book/curso é o seu mapa completo para construir e garantie seu futuro financeiro dashboards e aplicações de diarias usando apenas caneta o planner e sua disposição.
    Com esse planner, o poder dos seus mimos está a uma `pagina` de distância.

    **Recursos Principais:**
    - **Módulos Essenciais**: Aprenda a usar os widgets mais importantes.
    - **Visualização de Dados**: Integre bibliotecas como Matplotlib, Plotly e Altair.
    - **Implantação Simples**: Guia passo a passo para colocar sua aplicação no ar.
    - **Melhores Práticas**: Dicas de performance e design para apps incríveis.
    """)

with col2:
    # --- 3. Imagens (Placeholder) ---
    st.image("https://via.placeholder.com/300x200?text=Capa+do+Produto", caption="Capa do Guia Definitivo")
    st.markdown("---")

# --- 7. Preços e Promoções ---
st.header("Preço e Oferta Especial")
st.markdown("~~R$ 297,00~~")
st.markdown("## **R$ 97,00** por tempo limitado!")
st.markdown("Aproveite o desconto de lançamento de **67%**!")
st.markdown("---")

# --- 4. Botões de Ação (CTA) ---
st.header("Pronto para Começar?")
if st.button("Comprar Agora e Acessar Imediatamente!", use_container_width=True, type="primary"):
    st.success("Redirecionando para a página de checkout... (Link simulado)")
    # Link real seria: st.markdown("[Clique aqui para Comprar](SUA_URL_DE_CHECKOUT)")

if st.button("Saiba Mais (Download do Conteúdo Programático)", use_container_width=True):
    st.info("Baixando o conteúdo programático... (Ação simulada)")
    # Ação real seria: st.markdown("[Clique aqui para Baixar](SUA_URL_DO_PDF)")

st.markdown("---")

# --- 6. Testemunhos de Clientes ---
st.header("O Que Nossos Clientes Dizem")

# Usando um container para agrupar os testemunhos
with st.container(border=True):
    st.markdown("**⭐ 5 Estrelas!**")
    st.markdown("> *\"Eu estava lutando para compartilhar meus modelos de Machine Learning. O Guia Streamlit me deu a solução mais rápida e elegante! Recomendo!\"* - **Ana C.**, Cientista de Dados.")

with st.container(border=True):
    st.markdown("**⭐ 5 Estrelas!**")
    st.markdown("> *\"Conteúdo direto ao ponto e cheio de exemplos práticos. Meu primeiro app Streamlit foi ao ar em menos de um dia!\"* - **Bruno F.**, Desenvolvedor Python.")

st.markdown("---")

# --- 5. Formulário de Contato ---
st.header("Fale Conosco")
st.write("Tem alguma dúvida antes de comprar? Envie-nos uma mensagem!")

# O formulário Streamlit é simples, mas funcional
with st.form("form_contato"):
    nome = st.text_input("Seu Nome")
    email = st.text_input("Seu Melhor Email")
    mensagem = st.text_area("Sua Mensagem")

    # Botão de submissão do formulário
    submitted = st.form_submit_button("Enviar Mensagem", type="secondary")

    if submitted:
        # Aqui você integraria com um serviço de e-mail ou banco de dados
        st.success(f"Obrigado, {nome}! Sua mensagem foi enviada com sucesso. Responderemos em breve para {email}.")
        # st.json({"nome": nome, "email": email, "mensagem": mensagem}) # Para debug

st.markdown("---")

# --- Rodapé ---
st.caption("© 2025 Guia Streamlit. Todos os direitos reservados. | Política de Privacidade")