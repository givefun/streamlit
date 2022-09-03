# 스트림릿 라이브러리를 사용하기 위한 임포트
import streamlit as st
import pandas as pd

# 웹 대시보드 개발 라이브러리인 스트림릿은,
# main 함수가 있어야 한다.

def main() :
    st.title('안녕하세요. 100억 부자님!')
    st.write('## 당신은 사랑받기 위해 태어난 사람입니다.')
    st.markdown('Streamlit is **_really_ cool**.')
    
    view = [100, 150, 200]

    st.bar_chart(data=view)
    
    sview = pd.Series(view)
    sview

if __name__ == '__main__' :
    main()