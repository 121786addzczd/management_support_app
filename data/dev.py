import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

"""
## 「月次データ.py」の作成
"""

# エクセルデータの読み込み
drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", 
                        sheet_name="drink", engine="openpyxl", index_col=0)

"""
### 読み込んだエクセルデータの確認
"""
drink_data # マジックコマンド

# 月のリストを取得
print(drink_data.columns.values.tolist())

"""
#### 販売月もセレクトボックスを作成
"""
select_month = st.selectbox("月を選んでください", # 第１引数
                            drink_data.columns.values.tolist(), # 第２引数：月名を取得したリスト
                            )
select_month # マジックコマンド

"""
#### 選択した月の売上データを表示
"""
drink_data[select_month] # マジックコマンド

"""
#### 選択した月の売上データの棒グラフを表示
"""
st.bar_chart(drink_data[select_month])

"""
#### st.altair_chartを使って書いた棒グラフの完成形
"""

st.write(select_month) # わかりやすいように選んだ月を表示する
drink_data_dict = drink_data.to_dict()
data = pd.DataFrame({
    "メニュー": drink_data_dict[select_month].keys(),
    "数量": drink_data_dict[select_month].values()
})

# ここでは「棒グラフの設定」と「グラフの表示」を一緒に書いてコードをすっきりさせている
st.altair_chart(alt.Chart(data).mark_bar().encode(
    x=alt.X('メニュー', sort=None),
    y='数量',
    ),
    use_container_width=True)

"""
#### st.altair_chart用に用意したデータフレームの確認
"""
data # マジックコマンド

"""
#### エクセルで読み込んだdrink_dataをto_drictメソッドで辞書に変換
"""
drink_data_dict = drink_data.to_dict()
drink_data_dict # マジックコマンド。辞書で変換したdrink_dataの確認

# st.selectboxで選んだ月の"メニュー"と"数量"が取得できるか確認
print("メニュー名", drink_data_dict[select_month].keys())
print("数量", drink_data_dict[select_month].values())

"""
#### 作り直したデータフレームをst.altair_chartで表示
"""
# 辞書から作ったkeysとvaluesでデータフレームを作る
data = pd.DataFrame({
                    "メニュー":drink_data_dict[select_month].keys(),
                    "数量":drink_data_dict[select_month].values()
                    })
# st.altair_chartで棒グラフを表示(ソート変更なし)
st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)

"""
#### コメント登録機能の完成形
"""
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

"""
#### st.text_inputでコメントを入力して表示する
"""
comment = st.text_input("コメントを記入してください")
comment

"""
#### with構文を使い、st.formとst.form_submit_buttonで「登録」ボタンを作成する
"""
with st.form(key='test1'):
    submit_btn = st.form_submit_button("登録")
    submit_btn

"""
#### 「登録」ボタンを押したら、st.text_inputで入力したテキストを表示する
"""
with st.form(key='test2'):
    comment = st.text_input("コメントを記入してください")
    submit_btn = st.form_submit_button("登録")
    if submit_btn:
        st.write(f"{comment}")

"""
#### 「登録」ボタンを押下したら、st.text_inputで入力したテキストを「monthly_sales_comment.txt」に書き込む
"""
with st.form(key="test3"):
    comment = st.text_input("コメントを記入してください")
    submit_btn = st.form_submit_button("登録")
    if submit_btn:
        with open("./data/sales_data/monthly_sales_comment.txt", "a") as f:
            f.write(f"{comment}")
            st.write("登録した内容がmonthly_sales_comment.txtに書き込まれいるかどうか確認してください")

"""
#### 「登録」ボタンを押下したら、st.text_inputで入力した内容が「monthly_comment.txt」に追加される。
#### 併せて「monthly_sales_comment.txt」の内容を常に表示する。
"""
# コメント
with st.form(key='test4'):
    # textbox
    comment = st.text_input("コメントを記入してください")
    submit_btn = st.form_submit_button("登録")
    if submit_btn : # ボタンをクリックしたらコメントを登録する
        with open("./data/sales_data/monthly_sales_comment.txt", "a") as f:
            f.write(f"{comment}")
    with open("./data/sales_data/monthly_sales_comment.txt", "r") as f:
        sales_comment = f.read()
        st.write(sales_comment)
        

"""
#### monthly_drink_sales()関数を作成し、チェックボックスで呼び出す
"""
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
    
# タイトル
st.markdown(' ### 月次データ')

# ドリンクの月別売上のチェックボックス
if st.checkbox("ドリンク"):
    monthly_drink_sales()


"""
#### drinkの商品ごとのラジオボタンと品別売上の棒グラフを作成
"""
#エクセルデータの読み込み
drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="drink", 
                                engine="openpyxl", index_col=0)
# 行と列を入れ替える
transposed_drink_data = drink_data.transpose()
# 2カラム作成
col_1, col_2 = st.columns(2)
with col_1:
    # ラジオボタン作成
    selected_drink = st.radio("メニューを選んでください",
        transposed_drink_data.columns.unique(),
        key=4)
with col_2:
    # データフレーム作成
    data = pd.DataFrame({
        "営業月": transposed_drink_data.index.unique(), #月を取得
        "売上数": transposed_drink_data[selected_drink]
    })
    st.subheader(selected_drink)
    # 棒グラフの作成
    st.altair_chart(alt.Chart(data).mark_bar().encode(
        x=alt.X('営業月', sort=None),
        y='売上数',
    ),
    use_container_width=True)

"""
#### transposed_drink_dataの中身の確認
"""
transposed_drink_data # マジックコマンド

"""
#### ドリンクメニューのラジオボタン作成
"""
selected_drink = st.radio("メニューを選んでください",
                transposed_drink_data.columns.unique(),
                key="test5")
selected_drink # マジックコマンド

"""
#### transposed_drink_data.columns.unique()の中身
"""
st.write(transposed_drink_data.columns.unique())

"""
### ラジオボタンで選択された商品の売上数が出力されるか確認
"""
col_1, col_2 = st.columns(2)
with col_1:
    # ラジオボタン作成
    selected_drink = st.radio("メニューを選んでください",
        transposed_drink_data.columns.unique(),
        key="test6")
with col_2:
    st.write(transposed_drink_data[selected_drink])

"""
#### ラジオボタンで選択された商品の売上数が棒グラフで出力されるか確認
"""
col_1, col_2 = st.columns(2)
with col_1:
    # ラジオボタン作成
    selected_drink = st.radio("メニューを選んでください",
        transposed_drink_data.columns.unique(),
        key="test7")
with col_2:
    # データフレーム作成
    data = pd.DataFrame({
        "営業月": transposed_drink_data.index.unique(), #月を取得
        "売上数": transposed_drink_data[selected_drink]
    })
    st.subheader(selected_drink)
    # 棒グラフの描画
    st.altair_chart(alt.Chart(data).mark_bar().encode(
        x=alt.X('営業月', sort=None),
        y='売上数',
    ),
    use_container_width=True)


"""
#### チェックボックスにチェックを入れると、ラジオボタンで選択された商品の売上数が棒グラフで出力されるか確認
"""
def drink_kind():
    #エクセルデータの読み込み
    drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="drink", 
                                    engine="openpyxl", index_col=0)
    # 行と列を入れ替える
    transposed_drink_data = drink_data.transpose()

    # 2カラム作成
    col_1, col_2 = st.columns(2)
    with col_1:
        # ラジオボタン作成
        selected_drink = st.radio("メニューを選んでください",
            transposed_drink_data.columns.unique(),
            key="test8")
    with col_2:
        # データフレーム作成
        data = pd.DataFrame({
            "営業月": transposed_drink_data.index.unique(), #月を取得
            "売上数": transposed_drink_data[selected_drink]
        })
        st.subheader(selected_drink)
        # 棒グラフの描画
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('営業月', sort=None),
            y='売上数',
        ),
        use_container_width=True)

# ドリンクの品別売上
if st.checkbox("ドリンクの品別売上"):
    drink_kind()


"""
#### マルチセレクトを使用して、選択したドリンクメニューの売上数を線グラフで確認
"""

# タイトル
st.markdown(" #### ドリンクメニュー売上数比較")
#エクセルデータの読み込み
drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="drink",
                                engine="openpyxl", index_col=0)
# 行と列を入れ替える
transposed_drink_data = drink_data.transpose()
# マルチセレクトの作成
multiselected_drink_list = st.multiselect(
    "確認したいドリンクのメニューを選んでください（複数選択可）",
    transposed_drink_data.columns.unique(),
    "生大"
)
st.write(transposed_drink_data[multiselected_drink_list])
if not multiselected_drink_list:
    st.error("表示するメニューが選択されていません")
else:
    fig = px.line(transposed_drink_data, x=transposed_drink_data.index, y=multiselected_drink_list)
    st.plotly_chart(fig)