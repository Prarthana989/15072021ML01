import tkinter as tk
from csv import writer
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv('ml-100k/u.data',sep='\t',names=['user_id','item_id','rating','ts'])
items =pd.read_csv('ml-100k/u.item',sep='|',encoding='latin-1', names=['item_id','movie_title','year']+[str(i) for i in range(21)])
ml = pd.merge(data.drop('ts',axis=1), items[['item_id','movie_title']], on='item_id')
rating = pd.DataFrame(ml.groupby('movie_title')['rating'].mean())
rating['count'] = ml.groupby('movie_title')['rating'].count()
pt = ml.pivot_table(index='user_id', columns='movie_title',values='rating')
app = tk.Tk(__name__)
app.title("Movie Recommender")
app.geometry("500x300")
app.configure(bg='#856ff8')
movie_name = tk.Variable(app)
movie_name.set('')

tk.Label(app,text="Enter Movie name").place(x=0,y=10)
tk.Entry(app,textvariable=movie_name,font = ('Arial',15)).place(x=0,y=30)

tk.Label(app,text="Recomendded movie is: ").place(x=0,y=130)

def get_movie(m):
    query = m
    try:
        movie = [c for c in pt.columns if query.lower() in c.lower()]
        sim_mat = pd.DataFrame(pt.corrwith(pt[movie[0]]).dropna(),columns=['Corr'])
        sim_mat['rating'] = rating['rating']
        sim_mat['count'] = rating['count']
        query_rating = rating['rating'][movie].values[0]
        rec = sim_mat[(sim_mat['rating']>=query_rating)&(sim_mat['count']>100)].sort_values('Corr',ascending=False).head().index
        rec = [r for r in rec if r not in movie]
        return rec[0]
    except IndexError:
        return "Sorry! Try Another Movie"

def Submit():
    movie = movie_name.get()
    print("Submitted")
    tk.Label(app,text='').place(x=130,y=130)
    result=get_movie(movie)
    tk.Label(app,text=result).place(x=135,y=130)
    
tk.Button(app,text="Submit",command = Submit).place(x=0,y=80)
app.mainloop()
