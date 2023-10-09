import streamlit as st
import pandas as pd
import altair as alt


def monthly_drink_sales():
    #エクセルデータの読み込み
    drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="drink", 
                                    engine="openpyxl", index_col=0)
    #販売月のセレクトボックスを作成
    select_month = st.selectbox("月を選んでください",
                                drink_data.columns.values.tolist(),
                                key="drink")
    #読み込んだエクセルデータを辞書型に変更
    drink_data_dict = drink_data.to_dict()
    #辞書に変換されたドリンクのデータから、選択された月のデータフレームを作成
    data = pd.DataFrame({
                        "メニュー": drink_data_dict[select_month].keys(),
                        "数量": drink_data_dict[select_month].values(),
                        })
    #選択された月のデータフレームとグラフを表示
    st.subheader(f"{select_month}のドリンク販売実績")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:     
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)


# 肉類の月別売上の関数
def monthly_meat_sales():
    #エクセルデータの読み込み
    drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="meat", 
                                    engine="openpyxl", index_col=0)
    #販売月のセレクトボックスを作成
    select_month = st.selectbox("月を選んでください",
                                drink_data.columns.values.tolist(),
                                key="meat")
    #読み込んだエクセルデータを辞書型に変更
    drink_data_dict = drink_data.to_dict()
    #辞書に変換されたドリンクのデータから、選択された月のデータフレームを作成
    data = pd.DataFrame({
                        "メニュー": drink_data_dict[select_month].keys(),
                        "数量": drink_data_dict[select_month].values(),
                        })
    #選択された月のデータフレームとグラフを表示
    st.subheader(f"{select_month}の肉類販売実績")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:     
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)


def monthly_sidemenu_sales():
    #エクセルデータの読み込み
    drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="sidemenu", 
                                    engine="openpyxl", index_col=0)
    #販売月のセレクトボックスを作成
    select_month = st.selectbox("月を選んでください",
                                drink_data.columns.values.tolist(),
                                key="sidemenu")
    #読み込んだエクセルデータを辞書型に変更
    drink_data_dict = drink_data.to_dict()
    #辞書に変換されたドリンクのデータから、選択された月のデータフレームを作成
    data = pd.DataFrame({
                        "メニュー": drink_data_dict[select_month].keys(),
                        "数量": drink_data_dict[select_month].values(),
                        })
    #選択された月のデータフレームとグラフを表示
    st.subheader(f"{select_month}のサイドメニュー販売実績")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:     
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)


# タイトル
st.markdown(' ### 月次データ')

# ドリンクの月別売上のチェックボックス
if st.checkbox("ドリンク"):
    monthly_drink_sales()

# 肉類の月別売上のチェックボックス
if st.checkbox("肉類"):
    monthly_meat_sales()

# サイドメニューの月別売上のチェックボックス
if st.checkbox("サイドメニュー"):
    monthly_sidemenu_sales()

# コメント
with st.form(key='monthly_sales_comment'):
    # textbox
    comment = st.text_input("コメントを記入してください")
    submit_btn = st.form_submit_button("登録")
    if submit_btn : # ボタンをクリックしたらコメントを登録する
        with open("./data/sales_data/monthly_sales_comment.txt", "a") as f:
            f.write(f"{comment}")
    with open("./data/sales_data/monthly_sales_comment.txt", "r") as f:
        sales_comment = f.read()
        st.write(sales_comment)
st.markdown(":red[今回は練習用にデータベースの代わりにtxtファイルを使用してます。]")
st.markdown(":red[また今回はコメント登録後の取り消し機能を実装していません。]")
st.markdown(":red[monthly_sales_comment.txtを直接編集することは可能です。]")