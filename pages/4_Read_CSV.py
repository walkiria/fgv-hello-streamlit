from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code

# LOGGER = get_logger(__name__)


# df = pd.read_csv("./datasets/titanic.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

# st.title("Quem estava no titanic!")  # add a title
# st.write(df)  # visualize my dataframe in the Streamlit app

# fig, ax = plt.subplots()
# df.hist(
#     bins=8,
#     column="Age",
#     grid=False,
#     figsize=(8, 8),
#     color="#86bf91",
#     zorder=2,
#     rwidth=0.9,
#     ax=ax,
# )
# st.write(fig)


def data_frame_demo():
    @st.cache_data
    def get_UN_data():
        # AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv("./datasets/titanic.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
        df = df[['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']]
        return df.set_index("Survived").head(100)

    try:
        df = get_UN_data()
        df['Age'] = df['Age'].fillna(-1)
        df = df.astype({"Age": "Int64"},errors= "ignore")
        st.write(df.Age.min())
        passengers = st.multiselect(
            "Choose Passengers", list(df.index), [0,1]
        )
        if not passengers:
            st.error("Please select at least one passenger.")
        else:
            data = df.loc[passengers]
            # data /= 1000000.0
            st.write("### Ages", data.sort_index())

            # data = data.T.reset_index()
            data = data[['Age']]
            # data = pd.melt(data, id_vars=["index"]).rename(
            #     columns={"index": "Surviver", "value": "Age"}
            # )
            st.bar_chart(data)

            # st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )


st.set_page_config(page_title="Read CSV", page_icon="📊")
st.markdown("# Read CSV")
st.sidebar.header("Read CSV")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)

data_frame_demo()

