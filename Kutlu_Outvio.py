#!/usr/bin/env python
# coding: utf-8

# # M.Kutlu ŞENGÜL Test Task For Outvio-Python

# ## Import Packages and Libraries

# In[1]:


pip install sidetable


# In[2]:


import pandas as pd
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sn
import os
import plotly.graph_objs as go
import plotly.offline as py
import warnings
warnings.filterwarnings("ignore")
from IPython.core.display import HTML,display
import re
import sidetable 
import datetime as dt
import seaborn as sns
import plotly.express as px
py.init_notebook_mode(connected=True)
pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 9999
pd.options.display.float_format = '{:20,.2f}'.format


# # Import Shipments Data

# In[3]:


shipments_data = pd.read_excel('C:/Users/mkutl/Documents/GitHub/test_task/shipments.xlsx').fillna(0)


# ## Print First 15 Recods From Shipments Data

# In[4]:


shipments_data.head(15)


# ## Check Total Records in Shipments Data

# In[5]:


#checking the number of rows and columns
rows,columns=shipments_data.shape[0],shipments_data.shape[1]
display(HTML(f"<h3>  <b style='color:blue;font-size:21px;'>Inference for Shipments Data </b>:<ul><li>There are {rows} rows and {columns} columns.</li></ul></h3>"))


# ## Check Data and DataType

# In[6]:


#variables and dataypes
pd.DataFrame(shipments_data.dtypes)


# In[7]:


print(shipments_data.info()) 


# In[8]:


# checking for duplicate instances
no_of_duplicates=shipments_data.duplicated().sum()
display(HTML(f"<h3>  <b style='color:darkblue;font-size:21px;'>Inference for Shipments Data </b>:<ul><li>There are {no_of_duplicates} duplicate values.</li></ul></h3>"))


# In[9]:


# checking for NaN instances
no_of_nan_values=shipments_data.isna().sum().sum()
display(HTML(f"<h3>  <b style='color:red;font-size:21px;'>Inference for Shipments Data </b>:<ul><li>There are {no_of_nan_values} nan values.</li></ul></h3>"))


# In[10]:


## Last 15 data row
shipments_data.tail(15)


# ## Import Packages Data

# In[11]:


packages_data = pd.read_excel('C:/Users/mkutl/Documents/GitHub/test_task/packages.xlsx').fillna(0)


# In[12]:


packages_data.head()


# ## Print First 15 Recods from Packages Data

# In[13]:


packages_data.head(15)


# ## Check Total Records in Packages Data

# In[14]:


#checking the number of rows and columns
rows,columns=packages_data.shape[0],packages_data.shape[1]
display(HTML(f"<h3>  <b style='color:blue;font-size:25px;'>Inference for Packages Data </b>:<ul><li>There are {rows} rows and {columns} columns.</li></ul></h3>"))


# In[15]:


# checking for duplicate instances
no_of_duplicates=packages_data.duplicated().sum()
display(HTML(f"<h3>  <b style='color:blue;font-size:21px;'>Inference for Packages Data </b>:<ul><li>There are {no_of_duplicates} duplicate values.</li></ul></h3>"))


# In[16]:


print(packages_data.info()) 


# ## Import Products Data

# In[17]:


products_data = pd.read_excel('C:/Users/mkutl/Documents/GitHub/test_task/products.xlsx').fillna(0)


# In[18]:


products_data.head()


# ## Check Total Records in Products Data

# In[19]:


#checking the number of rows and columns
rows,columns=products_data.shape[0],packages_data.shape[1]
display(HTML(f"<h3>  <b style='color:blue;font-size:21px;'>Inference for Products Data </b>:<ul><li>There are {rows} rows and {columns} columns.</li></ul></h3>"))


# In[20]:


# checking for duplicate instances
no_of_duplicates=products_data.duplicated().sum()
display(HTML(f"<h3>  <b style='color:blue;font-size:21px;'>Inference for Products Data </b>:<ul><li>There are {no_of_duplicates} duplicate values.</li></ul></h3>"))


# In[21]:


print(products_data.info()) 


# ## Shipments Data Describes

# In[22]:


pd.DataFrame(shipments_data.describe().T)


# ## Packages Data Describes

# In[23]:


pd.DataFrame(packages_data.describe().T)


# ## Products Data Describes

# In[24]:


pd.DataFrame(products_data.describe().T)


# ## Total 10 Courier Count With Graph

# In[25]:


shipments_data = shipments_data.dropna()
ItemCount = shipments_data["courier"].value_counts().nlargest(10)
print("Top 10 Courier Count \n")
print(ItemCount)
sn.set_context("talk",font_scale=1)
plt.figure(figsize=(15,5))
sn.countplot(shipments_data['courier'],order = shipments_data['courier'].value_counts().nlargest(10).index)
plt.title('Top 10 Courier Count \n')
plt.ylabel('Total Count')
plt.xlabel('Courier Name')


# ## Top 5 Shipping Method 

# In[26]:


Shippingmethod = shipments_data["method"].value_counts().nlargest(5)
labels = (np.array(Shippingmethod.index))
sizes = (np.array((Shippingmethod / Shippingmethod.sum())*100))

trace = go.Pie(labels=labels, values=sizes)
layout = go.Layout(title="Top 5 Shipping Method")
dat = [trace]
fig = go.Figure(data=dat, layout=layout)
py.iplot(fig, filename="method")


# In[27]:


shipments_data.stb.freq(['courier'], value='cost', style=True, cum_cols=False)


# ## Data Cleaning for Merge DataSets Process

# In[28]:


pd.DataFrame(packages_data['products'].head(10))


# In[29]:


##clean_chars = ["!",'"',"#","%","&","'","(",")",
           ##   "*","+",",","-",".","/",":",";","<",
           ##   "=",">","?","@","[","\\","]","^","_",
           ##   "`","{","|","}","~","–","oid","$"]


# In[30]:


## for char in clean_chars:
   ## packages_data['products'] = packages_data['products'].str.replace(char, ' ')


# In[31]:


##pd.DataFrame(packages_data['products'].head(10))


# In[32]:


### for char in clean_chars:
   ## shipments_data['packages_id'] = shipments_data['packages'].str.replace(char, ' ')


# In[33]:


## for char in clean_chars:
   ## packages_data['products_id'] = packages_data['products'].str.replace(char, ' ')


# In[34]:


##split_packages_product_id=packages_data['products'].split(",")
##split_shipments_packages_id=shipments['packages'].split(",")


# In[35]:


#shipments_data['products']= shipments_data['products'].append.transpose()
#packages_data['products'] = packages_data['products'].append.transpose()


# ## Created Clean ID (Shipments & Packages Data Sets)--for Merging

# In[36]:


shipments = pd.read_excel('C:/Users/mkutl/Documents/GitHub/test_task/shipments_cleanid.xlsx').fillna(0)


# In[37]:


shipments.head()


# In[38]:


packages = pd.read_excel('C:/Users/mkutl/Documents/GitHub/test_task/packages_cleanid.xlsx').fillna(0)


# In[39]:


packages.head()


# In[40]:


df1_merged=pd.merge(shipments, packages, how='left', left_on='Package_id', right_on='_id')


# In[41]:


products = pd.read_excel('C:/Users/mkutl/Documents/GitHub/test_task/products_cleanid.xlsx').fillna(0)


# In[42]:


products 


# In[43]:


df2_merged=pd.merge(df1_merged, products, how='left', left_on='_id_x', right_on='_id')


# In[44]:


df2_merged.head(5)


# ## Average delivery time Analyze Process

# In[45]:


##shipments_cleanid2 = shipments_data.loc[~shipments_data[deliverDate']!='0']


# In[46]:


shipp = pd.read_excel('C:/Users/mkutl/Documents/GitHub/test_task/shipments_cleanid2.xlsx').fillna(0)


# In[47]:


shipp['deliverytime_day']= (pd.to_datetime(shipp.deliverDate) - pd.to_datetime(shipp.createdAt)).dt.days


# In[49]:


# extract year, month, day and time from date feature for CreatedAt
shipp['year'] = pd.DatetimeIndex(shipp['createdAt']).year
shipp['date'] = pd.DatetimeIndex(shipp['createdAt']).date
shipp['time'] = pd.DatetimeIndex(shipp['createdAt']).time
shipp['month_name'] = pd.DatetimeIndex(shipp['date']).month_name()
shipp['day_name'] = pd.DatetimeIndex(shipp['date']).day_name()


# In[50]:


shipp


# ## Average Delivery Time Per Courier (Day)

# In[51]:



pd.DataFrame(shipp.groupby('courier')['deliverytime_day'].mean())


# ## Average delivery time per Ship Method (Day)

# In[52]:


pd.DataFrame(shipp.groupby('method')['deliverytime_day'].mean())


# In[53]:


corrmap = shipp.corr()
top=corrmap.index
plt.figure(figsize=(30,20))
g=sns.heatmap(shipp[top].corr(),annot=True,cmap="RdYlGn")


# In[54]:


packages2 = pd.read_excel('C:/Users/mkutl/Documents/GitHub/test_task/packages_cleanid.xlsx').fillna(0)


# In[56]:


shipp['createdAt'].max() # Calculating when the last order come to check recency


# In[58]:


(packages2.groupby('_id')['Product_id'].count())


# ## Average products per order

# In[59]:


products.info()


# In[60]:


# let's prepare the value for the x-axis
month_name = [month_name for month_name, df in shipp.groupby('month_name')]
# let's plot it
plt.figure(figsize=(24, 4)) # figuring the size
# makes bar plot 
plt.plot(month_name, shipp.groupby(['month_name']).count())
# xticks
plt.xticks(month_name)
# let's add grid
plt.grid(True)
# title
plt.title(
    'Month Order ', 
    fontname='monospace', weight='bold'
)
# x-label
plt.xlabel('Month Sales')
# y-label
plt.ylabel('Number of Orders');


# ## Product quantity values on order basis

# In[61]:


packages2[['_id', 'Product_id']].groupby(['_id']).count().reset_index()


# In[62]:


products.info()


# In[63]:


top_products = products.groupby('name').size().reset_index().rename(columns={0: 'Total'}).sort_values('Total', ascending=False).head()
fig = px.pie(top_products, values='Total', names='name', color_discrete_sequence=px.colors.sequential.RdBu, title='Top 5 ordering products brand/ Name')
fig.show()


# top_products = products.groupby('sku').size().reset_index().rename(columns={0: 'Total'}).sort_values('Total', ascending=False).head()
# fig = px.pie(top_products, values='Total', names='sku', color_discrete_sequence=px.colors.sequential.BuGn_r, title='Top 5 Products/ SKU')
# fig.show()

# In[64]:


df_status = df2_merged[['isDelivered', 'cost']]
fig = px.bar(data_frame=df_status, x='isDelivered', y='cost', color='isDelivered', title='Delivered-Costs')
fig.show()


# In[67]:


products_means = packages2[['_id','Product_id']].groupby('_id').mean().count()


# In[68]:


products_means.head()


# In[69]:


##late_df = shipp[(shipp['deliverDate']) > shipp['estimatedDeliverDate']]
#Late_df[Late_df['Order Status'] == 'COMPLETE']


# In[70]:


Total_prodc=packages2.groupby('_id')['Product_id'].sum().reset_index()


# In[71]:


Total_prodc


# In[90]:


Product_count=packages2['Product_id'].count()


# In[96]:


Packages_count=packages2['_id'].count()


# In[ ]:


avg_price = packages2.groupby('_id')(Product_count).agg(np.mean)


# In[ ]:


avg_product=int(Product_count / Packages_count)  --- 11411/4333=2.63


# In[75]:


order_cal_num =  packages2.groupby('_id')['_id'].count()


# In[76]:


print(order_cal_num)


# In[77]:


product_cal =  packages2.groupby('Product_id')['Product_id'].count()


# In[78]:


print(product_cal)


# In[ ]:


##packages2["Product_id"].mean()


# In[ ]:




