from jupyter_dash import JupyterDash
import pandas as pd
import plotly.express as px
import dash
import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go
from collections import Counter


app = dash.Dash(__name__)
server = app.server

df = pd.read_csv('https://raw.githubusercontent.com/shabeeb248/datas/main/ipl.csv')
df=df.dropna()



app.layout = html.Div(children=[
    html.Div(
        children=[
                  html.Img(src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/245px-Chennai_Super_Kings_Logo.svg.png",alt="IPL", style={'display': 'inline-block','width':'150px','margin-right':'20px'}),
        
        html.Img(src="https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Mumbai_Indians_Logo.svg/230px-Mumbai_Indians_Logo.svg.png", style={'display': 'inline-block','width':'150px','height':'150px','margin-left':'20px'}),
        html.Img(src="https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Kolkata_Knight_Riders_Logo.svg/175px-Kolkata_Knight_Riders_Logo.svg.png", style={'display': 'inline-block','width':'120px','height':'150px','margin-left':'20px'}),
        html.Img(src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2a/Royal_Challengers_Bangalore_2020.svg/160px-Royal_Challengers_Bangalore_2020.svg.png", style={'display': 'inline-block','width':'150px','height':'150px','margin-left':'20px'}),
        html.Img(src="https://upload.wikimedia.org/wikipedia/en/1/1c/Punjab_Kings_logo_2021.png", style={'display': 'inline-block','width':'150px','height':'150px','margin-left':'20px'}),
        html.Img(src="https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Sunrisers_Hyderabad.svg/250px-Sunrisers_Hyderabad.svg.png", style={'display': 'inline-block','width':'150px','margin-left':'20px'}),
        html.Img(src="https://www.pngall.com/wp-content/uploads/2017/04/Rajasthan-Royals-Logo-PNG.png", style={'display': 'inline-block','width':'150px','margin-left':'20px'}),
        

        
        ],style={'text-align': 'center','backgroundColor':'black'}
            ),
            html.H1(children='IPL Data Analysis', style={'text-align': 'center','color': 'black', 'fontSize': 45}),
    html.Div(children='2007-2018', style={'text-align': 'center','color': 'black', 'fontSize': 28}),
     
    html.Div([

          html.Div([
                    html.Label(['Choose a team:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                np.append(df['winner'].unique(),"All teams"),
                id='team',
                value="All teams"
            )
            
        ], style={'width': '48%', 'display': 'inline-block', 'fontSize': 24}),

        html.Div([
                   html.Label(['Choose a season:'],style={'font-weight': 'bold'}),
                    dcc.Dropdown(
                        np.append(df['year'].unique(),"All season"),
                        value="All season",
                        id="season-year",
                    ),
            
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block','fontSize': 24})
    ]),
    html.Div(dcc.Graph(id='graph-1')), 
    html.Div(dcc.Graph(id='graph-2')), 
    html.Div(dcc.Graph(id='graph-3')),
    html.Div(dcc.Graph(id='graph-4')),

    
])

@app.callback(
    [
    Output('graph-1', 'figure'),
    Output('graph-2', 'figure'),
    Output('graph-3', 'figure'),
    Output('graph-4', 'figure')
    ],
    Input(component_id='team', component_property='value'),
    Input(component_id='season-year', component_property='value')
    )
def update_figure(team,selected_year):
    

    if (team=='All teams' and selected_year=='All season'):
      df2=df.player_of_match.value_counts().reset_index().rename(
           columns={'index': 'player', 0: 'Man_Of_The_Match'})
      

      fig1 = px.histogram(df, x="winner",text_auto=True).update_xaxes(categoryorder="total descending")
      fig1.update_layout( height=500,title={'text': "Best Team based on wins",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig1.update_layout(template="plotly_dark")


      fig2 = px.histogram(df2.head(15), x="player",y="player_of_match",nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig2.update_layout( height=500,title={'text': "Best Player based on player of matches",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")

      fig2.update_layout(template="plotly_dark")



      fig3 = px.histogram(df, x="winner",y='win_by_runs',nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig3.update_layout( height=500,title={'text': "Teams Ranked On Total winning Runs",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")


      fig3.update_layout(template="plotly_dark")


      fig4 = px.histogram(df, x="venue",nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig4.update_layout( height=800,title={'text': "Best Winning Venues",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")


      fig4.update_layout(template="plotly_dark")
      
    elif(team=='All teams' and selected_year!='All season'):
      newdf = df[df.year == int(selected_year)]
      df5=newdf.player_of_match.value_counts().reset_index().rename(
           columns={'index': 'player', 0: 'Man_Of_The_Match'})
      
      fig1 = px.histogram(newdf, x="winner",text_auto=True).update_xaxes(categoryorder="total descending")
      fig1.update_layout( height=500,title={'text': "Top teams Based on wins",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig1.update_layout(template="plotly_dark")

      fig2 = px.histogram(df5.head(15), x="player",y="player_of_match",nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig2.update_layout( height=500,title={'text': "Best player based on player of the match award",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig2.update_layout(template="plotly_dark")

      fig3 = px.histogram(newdf, x="winner",y="win_by_runs",nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig3.update_layout( height=500,title={'text': "Top team Based on winning runs",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig3.update_layout(template="plotly_dark")

      fig4 = px.histogram(newdf, x="venue",nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig4.update_layout( height=500,title={'text': "Best Winning Venues",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig4.update_layout(template="plotly_dark")

    elif(team!='All teams' and selected_year=='All season'):

      newdf1 =df[df.winner == team]
      newdf2 = df[(df["team1"]==team) | (df["team2"]==team)]
      total_match=len(newdf2)
      winning_match=len(newdf1)
      lab = ['lose','win']
      val = [total_match-winning_match, winning_match]
      df6=newdf1.player_of_match.value_counts().reset_index().rename(
           columns={'index': 'player', 0: 'Man_Of_The_Match'})
      
    
      filtered_df1 =df[df.winner == team]
      toss_win_count = df[df.toss_winner==team]["winner"].count()
      win_and_toss_win_df = df[df.toss_winner==team]
      win_and_toss_count = win_and_toss_win_df[df.winner==team]["winner"].count()
      toss_not_win =  toss_win_count-win_and_toss_count
      
      values2 = [toss_win_count,toss_not_win] 
      labels2 = ["Won After Toss","Lose After Toss"]
    

      fig1=go.Figure(data=[go.Pie(labels=lab, values=val)])
      fig1.update_layout( height=500,title={'text': "Win VS Lose",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig1.update_layout(template="plotly_dark")
     
      fig2 = px.histogram(df6.head(15), x="player",y="player_of_match",nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig2.update_layout( height=500,title={'text': "Best player based on player of the match award",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig2.update_layout(template="plotly_dark")

      
      fig3=go.Figure(data=[go.Pie(labels=labels2, values=values2)])
      fig3.update_layout( height=500,title={'text': "Won after toss VS Lost after toss",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                               font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig3.update_layout(template="plotly_dark")

      fig4 = px.histogram(newdf1, x="venue",nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig4.update_layout( height=800,title={'text': "Best Winning Venues",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                               font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig4.update_layout(template="plotly_dark")

    else:
      filtered_df = df[df.year == int(selected_year)]
      filtered_df1 = filtered_df[df.winner == team]
      toss_win_count = filtered_df[df.toss_winner==team]["winner"].count()
      win_and_toss_win_df = filtered_df[df.toss_winner==team]
      win_and_toss_count = win_and_toss_win_df[filtered_df.winner==team]["winner"].count()
      toss_not_win =  toss_win_count-win_and_toss_count
      values1 = [filtered_df1["win_by_runs"].sum(),filtered_df1["win_by_wickets"].sum()]
      labels1 = ["win_by_runs","win_by_wickets"]
      values2 = [toss_win_count,toss_not_win] 
      labels2 = ["Won After Toss","Lose After Toss"]

      fig1 = go.Figure(data=[go.Pie(labels=labels1, values=values1)])
      fig1.update_layout( height=500,title={'text': "Win by Runs VS Win by Wickets",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig1.update_layout(template="plotly_dark")


      fig2 = go.Figure(data=[go.Pie(labels=labels2, values=values2)])
      fig2.update_layout( height=500,title={'text': "Won after toss VS Lost after toss",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig2.update_layout(template="plotly_dark")


      fig3 = px.histogram(filtered_df1, x="venue",nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig3.update_layout( height=500,title={'text': "Best Winning Venues",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig3.update_layout(template="plotly_dark")

      fig4 = px.histogram(filtered_df1, x="player_of_match",nbins=50,text_auto=True).update_xaxes(categoryorder="total descending")
      fig4.update_layout( height=500,title={'text': "Best player based on player of the match award",'y':0.95,'x':0.5,'xanchor': 'center','yanchor': 'top'},title_font_size=30,font_family="Courier New",
                                font_color="white",title_font_family="Times New Roman",title_font_color="white",legend_title_font_color="green")
      fig4.update_layout(template="plotly_dark")
      
    return fig1,fig2,fig3,fig4


if __name__ == '__main__':
    app.run_server(debug=True)
