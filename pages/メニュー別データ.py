import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import os


def display_menu_sales(menu_type: str) -> None:
    """
    指定されたメニュータイプの売上データを表示する関数

    Args:
    - menu_type (str): 表示するメニュータイプ（例: "drink", "meat", "sidemenu"）

    Returns:
    - None
    """

    # エクセルデータの読み込み
    data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name=menu_type, engine="openpyxl", index_col=0)
    
    # 行と列を入れ替える
    transposed_data = data.transpose()

    # 2カラム作成
    col_1, col_2 = st.columns(2)
    with col_1:
        # ラジオボタン作成
        selected_item = st.radio(f"{menu_type}のメニューを選んでください",
            transposed_data.columns.unique(),
            key=f"radio_{menu_type}")  # 動的にキー名を変更
    with col_2:
        # データフレーム作成
        data_frame = pd.DataFrame({
            "営業月": transposed_data.index.unique(),  # 月を取得
            "売上数": transposed_data[selected_item]
        })
        st.subheader(selected_item)
        # 棒グラフの描画
        st.altair_chart(alt.Chart(data_frame).mark_bar().encode(
            x=alt.X('営業月', sort=None),
            y='売上数',
        ),
        use_container_width=True)


def display_category_sales_chart(category: str = "drink", category_label: str = "ドリンク") -> None:
    """
    指定されたカテゴリの売上データを表示する関数

    Args:
    - category (str): 英語のカテゴリ名（例: "drink", "meat", "sidemenu"）
    - category_label (str): 日本語のカテゴリ表示名（例: "ドリンク", "肉", "サイドメニュー"）

    Returns:
    - None
    """

    # タイトル
    st.markdown(f"#### {category_label}メニュー売上数比較")
    
    # エクセルデータの読み込み
    data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name=category, engine="openpyxl", index_col=0)
    
    # 行と列を入れ替える
    transposed_data = data.transpose()
    # 初期の選択肢を設定 transposed_dataの最初のカラム名をデフォルトとして使用
    default_selection = transposed_data.columns[0] if not transposed_data.empty else None

    # マルチセレクトの作成
    multiselected_list = st.multiselect(
        f"確認したい{category}のメニューを選んでください（複数選択可）",
        transposed_data.columns.unique(),
        default_selection
    )
    
    st.write(transposed_data[multiselected_list])

    if not multiselected_list:
        st.error("表示するメニューが選択されていません")
    else:
        fig = px.line(transposed_data, x=transposed_data.index, y=multiselected_list)
        st.plotly_chart(fig)


def register_and_display_comments():
    """
    コメントをテキストボックスに登録し、登録されたコメントを表示する関数
    """
    
    dir_path = "./data/sales_data/"
    file_name = "sales_kind_comment.txt"
    file_path = dir_path + file_name
    
    # コメント入力フォーム
    # file_nameに.が二つ異常あることは想定していない
    with st.form(key=file_name.rsplit('.', 1)[0]):
        # textbox
        comment = st.text_input("コメントを記入してください")
        submit_btn = st.form_submit_button("登録")
        
        if submit_btn:  # ボタンをクリックしたらコメントを登録する
            with open(file_path, "a") as f:
                f.write(f"{comment}\n")
        
        with open(file_path, "r") as f:
            sales_comment = f.read()
            st.write(sales_comment)
    
    # 注意コメント
    st.markdown(":red[今回は練習用にデータベースの代わりにtxtファイルを使用してます。]")
    st.markdown(":red[また今回はコメント登録後の取り消し機能を実装していません。]")
    st.markdown(f":red[{file_name}を直接編集することは可能です。]")


def main():
    # タイトル
    st.markdown(' ### 品別売上')

    # ドリンクの品別売上
    if st.checkbox("ドリンクの品別売上"):
        display_menu_sales("drink", "ドリンク")

    # ドリンクの品別売上（マルチセレクト）
    if st.checkbox("ドリンクの品別売上（マルチセレクト）"):
        display_category_sales_chart("drink")

    # 肉類の品別売上
    if st.checkbox("肉類の品別売上"):
        display_menu_sales("meat")

    # 肉類の品別売上（マルチセレクト）
    if st.checkbox("肉類の品別売上（マルチセレクト）"):
        display_category_sales_chart("meat", "肉類")

    # サイドメニューの品別売上
    if st.checkbox("サイドメニューの品別売上"):
        display_menu_sales("sidemenu")

    # 肉類の品別売上（マルチセレクト）
    if st.checkbox("サイドメニューの品別売上（マルチセレクト）"):
        display_category_sales_chart("sidemenu", "サイドメニュー")

    register_and_display_comments()

if __name__ == "__main__":
    main()
