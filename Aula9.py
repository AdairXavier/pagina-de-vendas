import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Página de Vendas Exclusiva",
    page_icon="🚀",
    layout="wide", # Layout wide para melhor aproveitamento de tela em desktops
    initial_sidebar_state="collapsed"
)

# --- Estilo (nativo, limpo e moderno.) ---
# O planner é didatico, detalhado e intuitivo.
# este planner exclusivo oferece ferramentas poderosa.

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
    Este e-book/curso é o seu mapa completo para construir e garantir seu futuro financeiro e aplicações de diarias usando apenas caneta o planner e sua disposição.
    Com esse planner, o poder dos seus mimos está a uma `pagina` de distância.

    **Recursos Principais:**
    - **Módulos Essenciais**: Aprenda a usar o dinheiro a seu favor.
    - **Visualização de Dados**: FeedBack: tipos, objetivo e importancia.
    - **Implantação Simples**: Guia passo a passo para colocar sua aplicação em pratica.
    - **Melhores Práticas**: Dicas e como ter controle do seu dinheiro.
    """)

with col2:
    # --- 3. Imagens (Placeholder) ---
    st.image("https://via.placeholder.com/300x200?text=Capa+do+Produto", caption="Capa do Guia Definitivo")
    st.markdown("---")

# --- 7. Preços e Promoções ---
st.header("Preço e Oferta Especial")
st.markdown("~~R$ 987,00~~")
st.markdown("## **R$ 592,20** por tempo limitado!")
st.markdown("Aproveite o desconto de lançamento de **40%**!")
st.markdown("---")

# --- 4. Botões de Ação (CTA) ---
st.header("Pronto para Começar?")
if st.button("Comprar Agora e Acessar Imediatamente!", use_container_width=True, type="primary"):
    st.success("Redirecionando para a página de checkout... (Link simulado)")
    # Link real seria: st.markdown("[Clique aqui para Comprar](SUA_URL_DE_CHECKOUT)")

if st.button("Saiba Mais (Conteúdo Programático)", use_container_width=True):
    st.info("Baixando o conteúdo programático... (Ação simulada)")
    # Ação real seria: st.markdown("[Clique aqui para Baixar](SUA_URL_DO_PDF)")

st.markdown("---")

# --- 6. Testemunhos de Clientes ---
st.header("O Que Nossos Clientes Dizem")

# Usando um container para agrupar os testemunhos
with st.container(border=True):
    st.markdown("**⭐ 5 Estrelas!**")
    st.markdown("> *\"Simplicidade e Praticidade: Mesmo para quem não tem muito tempo, a simplicidade de uso do planner é um ponto positivo, facilitando a criação de um hábito de controle financeiro diário. O Guia financeiro me deu a solução mais rápida e elegante! Recomendo!\"* - **Ana C.**, Dona do studio Mulher Bela.")

with st.container(border=True):
    st.markdown("**⭐ 5 Estrelas!**")
    st.markdown("> *\"Conteúdo direto ao ponto e cheio de exemplos práticos. , após o uso do planner, consegui "colocar ordem na casa", evitar dívidas e até mesmo sair do vermelho, graças a um melhor controle financeiro.!\"* - **Bruno F.**, Desenvolvedor.")
with st.container(border=true):
st.markdown("**⭐ 5 Estrelas!**")
st.markdown("> *\"Controle de Gastos e Redução de Desperdícios, a eficácia do planner em ajudar a controlar gastos supérfluos e a reduzir desperdícios, o que leva a uma economia real no final do mês.!\"* - **Adair JS Xavier.**, Dev juninho.")

# --- 5. Formulário de Contato ---
st.header("Fale Conosco")
st.write("Tem alguma dúvida antes de comprar? Envie-nos uma mensagem!")

# O formulário é simples, mas funcional
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
st.caption("© 2025 Domine suas finanças. Guia definitivo para finanças: Luiza Xavier. Todos os direitos reservados. | Política de Privacidade")
