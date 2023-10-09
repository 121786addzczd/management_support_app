import streamlit as st

# タイトル
st.markdown(" ### 売上分析ダッシュボード")
# キャプション
st.caption("このダッシュボードでは月次データとメニュー別の売上数をインタラクティブに確認できます")

# 使用しているファイルの表示
expander1 = st.expander("使用しているファイル")
expander1.write("2022sales_data.xlsx")
expander1.write("2022financial_data.xlsx")
expander1.write("monthly_sales_comment.txt")
expander1.write("sales_kind_comment.txt")
expander1.caption("以上のデータは経理部で管理しています")

# 問い合わせ先の表示
expander2 = st.expander("メニューの中身に関する問い合わせ先")
expander2.write("事業部")
expander2.write("TEL: 03-xxxx-xxx0")

expander3 = st.expander("各種売上データに関する問い合わせ先")
expander3.write("経理部")
expander3.write("TEL: 03-xxxx-xxx1")


expander4 = st.expander("財務諸表に関する問い合わせ先")
expander4.write("経理部および経営企画部")
expander4.write("TEL: 03-xxxx-xxx1（経理部）")
expander4.write("TEL: 03-xxxx-xxx2（経営企画部）")

# 注意書き
st.markdown(":red[【注意事項】]")
st.markdown(":red[ここはシステム開発者の教育用ダッシュボードです。]")
st.markdown(":red[そのため、使用するデータは全て架空のデータです。]")
