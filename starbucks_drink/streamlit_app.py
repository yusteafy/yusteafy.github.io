import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("starbucks_drink//starbucks.csv")
df_header = list(df)

translations = {
    "EN": {
        "title": "Starbucks-Nutrition </br>Analysis",
        "beverage_category": "Beverage Category",
        "beverage": "Beverage",
        "beverage_prep": "Beverage Prep",
        "product_info": "Nutritional Information:",
        "top_products": "Number of products",
        "top_fiber": "Top {n} Products with Highest Dietary Fiber",
        "top_sugar": "Top {n} Products with Highest Sugars",
        "less20": "Less than 20g",
        "over20": "Greater than 20g",
        "saturated_fat_chart": "Distribution of Products by Saturated Fat",
        "fat_n_calo": "Total Fat and Calories",
        "fat_n_sugar": "Total Fat and Sugars",
        "DV": "Daily Values for Nutrients",
        "nutrien_value": "Nutrient Value"
    },
    "JP": {
        "title": "スターバックス</br>栄養分析",
        "beverage_category": "カテゴリー",
        "beverage": "飲料",
        "beverage_prep": "種類",
        "product_info": "栄養成分情報：",
        "top_products": "商品の数",
        "top_fiber": "食物繊維が最も多い上位 {n} 商品",
        "top_sugar": "糖分が最も多い上位 {n} 商品",
        "less20": "20g未満",
        "over20": "20g以上",
        "saturated_fat_chart": "飽和脂肪酸による商品の分布",
        "fat_n_calo": "総脂肪とカロリー",
        "fat_n_sugar": "総脂肪と糖分",
        "DV": "1日の栄養所要量",
        "nutrien_value": "栄養価"
    },
}

with st.columns(14)[13]:
    lang = st.selectbox('', ["EN", "JP"], key = 'lang')

t = translations[st.session_state.lang]

title = st.columns(2)
with title[0]:
    st.markdown(
        f"""
        <style>
            .title {{
                font-size: 100px;
                margin: 0;
                display: flex;
                justify-content: flex-end;
                align-items: center;
                height: 700px;
            }}
        </style>
        <div class = "title">{t['title']}</div>
        """,
        unsafe_allow_html = True
    )

with title[1]: 
    st.image('image/logo.png', width = 700)

Beverage_category_abbr = {
    'Coffee': 'Coffe',
    'Classic Espresso Drinks': 'Espresso',
    'Signature Espresso Drinks': 'Sign. Espresso',
    'Tazo Tea Drinks': 'Tazo',
    'Shaken Iced Beverages': 'Shaken Iced',
    'Smoothies': 'Smoothies',
    'Frappuccino Blended Coffee': 'Frappuccino',
    'Frappuccino Light Blended Coffee': 'Frappuccino Li.',
    'Frappuccino Blended Creme': 'Frappuccino Creme'
}

Beverage_abbr = {
    'Brewed Coffee': 'Brewed',
    'Caffe Latte': 'Latte',
    'Caffe Mocha (Without Whipped Cream)': 'Mocha (No Whip)',
    'Vanilla Latte (Or Other Flavoured Latte)': 'Vanilla Latte',
    'Caffe Americano': 'Americano',
    'Cappuccino': 'Cappuccino',
    'Espresso': '',
    'Skinny Latte (Any Flavour)': 'Skinny Latte',
    'Caramel Macchiato': 'Macchiato',
    'White Chocolate Mocha (Without Whipped Cream)': 'Choco. Mocha (No Whip)',
    'Hot Chocolate (Without Whipped Cream)': 'Hot Choco. (No Whip)',
    'Caramel Apple Spice (Without Whipped Cream)': 'Caramel Apple (No Whip)',
    'Tazo Tea': 'Tazo',
    'Tazo Chai Tea Latte': 'Chai Latte',
    'Tazo Green Tea Latte': 'Green Latte',
    'Tazo Full-Leaf Tea Latte': 'Leaf Latte',
    'Tazo Full-Leaf Red Tea Latte (Vanilla Rooibos)': 'Leaf Red Latte (Vanilla)',
    'Iced Brewed Coffee (With Classic Syrup)': 'Iced Brewed (Syrup)',
    'Iced Brewed Coffee (With Milk & Classic Syrup)': 'Brewed (Milk + Syrup)',
    'Shaken Iced Tazo Tea (With Classic Syrup)': 'Tazo (Syrup)',
    'Shaken Iced Tazo Tea Lemonade (With Classic Syrup)': 'Shaken Iced Tazo Tea Lemonade (Syrup)',
    'Banana Chocolate Smoothie': 'Banana Choco.',
    'Orange Mango Banana Smoothie': 'Orange Mango Banana',
    'Strawberry Banana Smoothie': 'Strawberry Banana',
    'Coffee': 'Coffe',
    'Mocha (Without Whipped Cream)': 'Mocha (No Whip)',
    'Caramel (Without Whipped Cream)': 'Caramel (No Whip)',
    'Java Chip (Without Whipped Cream)': 'Java Chip (No Whip)',
    'Mocha': 'Mocha',
    'Caramel': 'Caramel',
    'Java Chip': 'Java Chip',
    'Strawberries & Creme (Without Whipped Cream)': 'Strawberry (No Whip)',
    'Vanilla Bean (Without Whipped Cream)': 'Vanilla Bean (No Whip)',
}

find_image = {
	'Smoothies - Banana Chocolate Smoothie': 'image/sample.png',
	'Coffee - Brewed Coffee': 'image/Veranda_Blend_Hot.png',
	'Classic Espresso Drinks - Caffe Americano': 'image/coffe/CaffeAmericano.png',
	'Classic Espresso Drinks - Caffe Latte': 'image/coffe/CaffeLatte.png',
	'Classic Espresso Drinks - Caffe Mocha (Without Whipped Cream)': 'image/coffe/CaffeMocha.png',
	'Classic Espresso Drinks - Cappuccino': 'image/coffe/Cappuccino.png',
	'Frappuccino Light Blended Coffee - Caramel': 'image/frapp/CaramelFrapp.png',
	'Frappuccino Blended Coffee - Caramel (Without Whipped Cream)': 'image/frapp/CaramelFrapp.png',
	'Signature Espresso Drinks - Caramel Apple Spice (Without Whipped Cream)': 'image/coffe/CaramelMacchiato.png',
	'Signature Espresso Drinks - Caramel Macchiato': 'image/coffe/CaramelMacchiato.png',
	'Frappuccino Blended Coffee - Coffee': 'image/frapp/CoffeeFrapp.png',
	'Frappuccino Light Blended Coffee - Coffee': 'image/frapp/CoffeeFrapp.png',
	'Classic Espresso Drinks - Espresso': 'image/coffe/Espresso_Single.png',
	'Signature Espresso Drinks - Hot Chocolate (Without Whipped Cream)': 'image/coffe/SignatureHotChocolat.png',
	'Shaken Iced Beverages - Iced Brewed Coffee (With Classic Syrup)': 'image/ColdBrew.png',
	'Shaken Iced Beverages - Iced Brewed Coffee (With Milk & Classic Syrup)': 'image/ColdBrew.png',
	'Frappuccino Light Blended Coffee - Java Chip': 'image/frapp/JavaChipFrapp.png',
	'Frappuccino Blended Coffee - Java Chip (Without Whipped Cream)': 'image/frapp/JavaChipFrapp.png',
	'Frappuccino Light Blended Coffee - Mocha': 'image/frapp/MochaFrapp.png',
	'Frappuccino Blended Coffee - Mocha (Without Whipped Cream)': 'image/frapp/MochaFrapp.png',
	'Smoothies - Orange Mango Banana Smoothie': 'image/sample.png',
	'Shaken Iced Beverages - Shaken Iced Tazo Tea (With Classic Syrup)': 'image/IcedChaiTeaLatte.png',
	'Shaken Iced Beverages - Shaken Iced Tazo Tea Lemonade (With Classic Syrup)': 'image/IcedChaiTeaLatte.png',
	'Classic Espresso Drinks - Skinny Latte (Any Flavour)': 'image/coffe/CaffeLatte.png',
	'Frappuccino Blended Creme - Strawberries & Creme (Without Whipped Cream)': 'image/frapp/StrawberryFrapp.png',
	'Smoothies - Strawberry Banana Smoothie': 'image/sample.png',
	'Tazo Tea Drinks - Tazo Chai Tea Latte': 'image/ChaiBrewedTea.png',
	'Tazo Tea Drinks - Tazo Full-Leaf Red Tea Latte (Vanilla Rooibos)': 'image/ChaiBrewedTea.png',
	'Tazo Tea Drinks - Tazo Full-Leaf Tea Latte': 'image/ChaiBrewedTea.png',
	'Tazo Tea Drinks - Tazo Green Tea Latte': 'image/ChaiBrewedTea.png',
	'Tazo Tea Drinks - Tazo Tea': 'image/ChaiBrewedTea.png',
	'Frappuccino Blended Creme - Vanilla Bean (Without Whipped Cream)': 'image/frapp/VanillaBeanFrapp.png',
	'Classic Espresso Drinks - Vanilla Latte (Or Other Flavoured Latte)': 'image/coffe/VanillaCaffeLatte.png',
	'Signature Espresso Drinks - White Chocolate Mocha (Without Whipped Cream)': 'image/coffe/WhiteChocolateMocha.png',
}

## New headers does not appear in data franme
df['Full_Name'] = df['Beverage_category'] + " - " + df['Beverage'] + " (" + df['Beverage_prep'] + ")"
df['Short_Name'] = df['Beverage_category'].map(Beverage_category_abbr) + " - " + df['Beverage'].map(Beverage_abbr) + " (" + df['Beverage_prep'] + ")"

df['Caffeine (mg)'] = df['Caffeine (mg)'].replace('Varies', 0).astype(float)

df['Caffeine (g)'] = df['Caffeine (mg)'] / 1000
df['Sodium (g)'] = df['Sodium (mg)'] / 1000
df['Cholesterol (g)'] = df['Cholesterol (mg)'] / 1000

df['image'] = df['Beverage_category'] + " - " + df['Beverage']
df['image'] = df['image'].map(find_image)
##

beverage_categories = ["None"] + list(df['Beverage_category'].unique())
beverages = ["None"]
beverage_preps = ["None"]

col = st.columns(5)

with col[1]:
    selected_beverage_category = st.selectbox(t["beverage_category"], beverage_categories, key = 'beverage_category')

if selected_beverage_category != "None":
    filtered_df = df[df['Beverage_category'] ==  selected_beverage_category]
    beverages = ["None"] + list(filtered_df['Beverage'].unique())
else:
    filtered_df = df

with col[2]:
    selected_beverage = st.selectbox(t["beverage"], beverages, key = 'beverage')

if selected_beverage != "None":
    filtered_df = filtered_df[filtered_df['Beverage'] ==  selected_beverage]
    beverage_preps = ["None"] + list(filtered_df['Beverage_prep'].unique())
else:
    beverage_preps = ["None"] + list(filtered_df['Beverage_prep'].unique())

with col[3]:
    selected_beverage_prep = st.selectbox(t["beverage_prep"], beverage_preps, key = 'beverage_prep')

if selected_beverage_prep != "None":
    product_info = filtered_df[filtered_df['Beverage_prep'] ==  selected_beverage_prep]
else:
    product_info = filtered_df

st.write(t["product_info"])
st.dataframe(product_info, column_order = df_header)

if selected_beverage_category != "None" and selected_beverage != "None" and selected_beverage_prep != "None":
    cols = product_info.columns
    exclude_cols = ['Beverage_category', 'Beverage', 'Beverage_prep', 'Short_Name', 'Full_Name', 'Caffeine (g)', 'Sodium (g)', 'Cholesterol (g)', 'image']
    rows_to_display = [col for col in cols if col not in exclude_cols]

    for i in range(0, len(rows_to_display), 4):
        subcols = st.columns(4)
        cols_to_display = rows_to_display[i:i+4]
        for col, subcol in zip(cols_to_display, subcols):
            subcol.markdown(f"<div class = 'single-line'><strong>{col}:</strong> {product_info[col].values[0]}</div>", unsafe_allow_html = True)

        for j in range(len(cols_to_display), 4): # Empty columns 
            subcols[j].write("&nbsp;", unsafe_allow_html = True)

    product = st.columns(3)

    with product[0]:
        st.markdown(
            f"""
            <br>
            <h6><b>{product_info['Full_Name'].iloc[0]}</b></h6>
            """,
            unsafe_allow_html = True)
        st.image(filtered_df['image'].iloc[0], width = 300)

    with product[1]:
        st.markdown(
            f"""
            <style>
                .indent {{
                    padding-left: 1.8em
                }}
            </style>
            <br>
            <h6><b>{t["DV"]}</b></h6>
            <br>
            <p class = "indent"><b>Saturated Fat:</b> < 20g</p>
            <p class = "indent"><b>Sugar:</b> < 50g</p>
            <p class = "indent"><b>Sodium:</b> < 2.3g</p>
            <p class = "indent"><b>Caffeine:</b> < 0.4g</p>
            """,
            unsafe_allow_html = True)

    with product[2]:
        selected_product = product_info.iloc[0]
        nutrient_values = {
            'Nutrient': ['Sodium (g)', 'Saturated Fat (g)', 'Caffeine (g)', 'Sugars (g)'],
            'Value': [
                selected_product['Sodium (g)'],
                selected_product['Saturated Fat (g)'],
                selected_product['Caffeine (g)'],
                selected_product['Sugars (g)']
            ]
        }
        nutrient_df = pd.DataFrame(nutrient_values)

        row_fig = px.bar(nutrient_df, x = 'Nutrient', y = 'Value', title = t["nutrien_value"], color = 'Nutrient', text = 'Value', labels = {'Value': 'Value (g)'})

        st.plotly_chart(row_fig)
        
        # expand
        # on = st.toggle(t["product_info"])

        # if on:
        #     ex_cols = ['Total Fat (g)', 'Sodium (g)', 'Total Carbohydrates (g)', 'Cholesterol (g)', 'Dietary Fiber (g)', 'Sugars (g)', 'Protein (g)', 'Caffeine (g)']
        #     ex_info = product_info[ex_cols].iloc[0]

        #     pie_chart = px.pie(values = ex_info, names = ex_cols, title = None)

        #     st.plotly_chart(pie_chart)
        # else:

        # pie chart
        # nutrition_cols = ['Sodium (g)', 'Saturated Fat (g)', 'Caffeine (g)', 'Sugars (g)']
        # nutrition_info = product_info[nutrition_cols].iloc[0]

        # pie_chart = px.pie(values = nutrition_info, names = nutrition_cols, title = None)

        # st.plotly_chart(pie_chart)

scatter_fig = px.scatter(df, x = 'Total Fat (g)', y = 'Calories', title = t["fat_n_calo"])

if selected_beverage_category != "None" or selected_beverage != "None" or selected_beverage_prep != "None":
    for _, row in product_info.iterrows():
        scatter_fig.add_scatter(x = [row['Total Fat (g)']], y = [row['Calories']], mode = 'markers', marker = dict(color = 'red'), name = row['Short_Name'])
else:
    for _, row in df.iterrows():
        scatter_fig.add_scatter(x = [row['Total Fat (g)']], y = [row['Calories']], mode = 'markers', marker = dict(color = 'red'), name = row['Short_Name'])

with st.columns(2)[1]: # Slide bar for double bar graph
    start_index = st.slider('', 0, len(df)-10, 0)
    end_index = start_index + 10
    sliced_df = df.iloc[start_index:end_index]

side_graph = st.columns(2)

with side_graph[0]:
    st.plotly_chart(scatter_fig)

with side_graph[1]:
    double_bar_graph = go.Figure()

    double_bar_graph.add_trace(go.Bar(
        y = sliced_df['Short_Name'],
        x = sliced_df['Total Fat (g)'],
        name = 'Total Fat (g)',
        orientation = 'h',
        marker = dict(color='lightblue')
    ))

    double_bar_graph.add_trace(go.Bar(
        y = sliced_df['Short_Name'],
        x = -sliced_df['Sugars (g)'],
        name = 'Sugars (g)',
        orientation = 'h',
        marker = dict(color='lightcoral')
    ))

    double_bar_graph.update_layout(
        title = t["fat_n_sugar"],
        xaxis = dict(title = 'Grams'),
        yaxis = dict(title = 'Product'),
        barmode = 'relative',
        bargap = 0.15,
        bargroupgap = 0.1,
        showlegend = True
    )

    st.plotly_chart(double_bar_graph)
    
with st.columns(18)[0]:
    top_n = st.number_input(t["top_products"], min_value = 1, max_value = len(df), value = 5)

top_graph = st.columns(3)

with top_graph[0]:
    top_fiber = df.nlargest(top_n, 'Dietary Fiber (g)')
    fig_fiber = px.bar(top_fiber, x = 'Dietary Fiber (g)', y = 'Short_Name', orientation = 'h', title = t["top_fiber"].format(n = top_n))
    fig_fiber['layout']['yaxis']['autorange'] = "reversed"
    fig_fiber.update_layout(xaxis_title = 'Dietary Fiber (g)', yaxis_title = None)
    st.plotly_chart(fig_fiber)

with top_graph[1]:
    top_sugar = df.nlargest(top_n, 'Sugars (g)')
    fig_sugar = px.bar(top_sugar, x = 'Sugars (g)', y = 'Short_Name', orientation = 'h', title = t["top_sugar"].format(n = top_n))
    fig_sugar['layout']['yaxis']['autorange'] = "reversed"
    fig_sugar.update_layout(xaxis_title = 'Sugars (g)', yaxis_title = None)
    st.plotly_chart(fig_sugar)

with top_graph[2]:
    df['Saturated_Fat_Category'] = df['Saturated Fat (g)'].apply(
        lambda x: '0g' if x == 0 else (t["less20"] if x < 20 else t["over20"])
    )

    saturated_fat_counts = df['Saturated_Fat_Category'].value_counts().reset_index()
    saturated_fat_counts.columns = ['Saturated_Fat_Category', 'Count']

    sat_fat = px.pie(saturated_fat_counts, values = 'Count', names = 'Saturated_Fat_Category', title = t["saturated_fat_chart"], color_discrete_sequence = px.colors.qualitative.Pastel)
    st.plotly_chart(sat_fat)

# Pie chart for each product

# charts_per_row = 3
# charts = []

# for index, product in filtered_df.iterrows():
#     labels = ['Total Carbohydrates (g)', 'Dietary Fiber (g)', 'Sugars (g)', 'Caffeine (mg)']
#     values = [product['Total Carbohydrates (g)'], product['Dietary Fiber (g)'], product['Sugars (g)'], product['Caffeine (mg)']]

#     fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
#     fig.update_layout(title_text = f'{product["Short_Name"]}')

#     charts.append(fig)

# for i in range(0, len(charts), charts_per_row):
#     row_charts = charts[i:i + charts_per_row]
#     cols = st.columns(charts_per_row)

#     for col, chart in zip(cols, row_charts):
#         col.plotly_chart(chart)