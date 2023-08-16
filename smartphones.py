#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import warnings 

warnings.filterwarnings('ignore')


# In[8]:


#read data
data=pd.read_csv(r'C:\Users\rtxeg\Downloads\smartphones.csv')
data.head()


# # basic analysis
# 

# In[9]:


data.shape


# In[10]:


data.info()


# In[13]:


data.isna().sum()


# In[14]:


data.describe()


# # brand vs number model

# In[15]:


brand_count=data.brand_name.value_counts().reset_index()
brand_count


# In[68]:


plt.figure(figsize=(15,6),dpi=200)
sns.barplot(data=brand_count.head(20),x='index',y='brand_name',palette='winter')
plt.title('brand name according to number',fontweight='bold',fontsize=25,color='blue')
plt.xlabel('brand name',fontweight='bold',fontsize=20,color='blue',labelpad=10)
plt.ylabel('number',fontweight='bold',fontsize=20,color='blue',labelpad=10)
plt.xticks(rotation=90,fontsize=15,color='blue')
plt.yticks(fontsize=15,color='blue')
plt.show()


# # brand vs average price 

# In[26]:


avg_price=data.groupby('brand_name')['price'].mean().reset_index()
avg_price=avg_price.sort_values(by='price',ascending=False)
avg_price


# In[37]:


plt.figure(figsize=(14,6),dpi=300)
sns.barplot(data=avg_price.head(10),x='brand_name',y='price',width=.6,palette='icefire')
plt.title('most 10 expensive brands',color='green',fontweight='bold',fontsize=26)
plt.xlabel('brand',color='green',fontweight='bold',fontsize=20,labelpad=10)
plt.ylabel('price',color='green',fontweight='bold',fontsize=20,labelpad=10)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


# # brand vs avg rating 

# In[29]:


avg_rating = data.groupby('brand_name')['avg_rating'].mean().reset_index()
avg_rating = avg_rating.sort_values(by='avg_rating',ascending=False)
avg_rating.head()


# In[36]:


plt.figure(figsize=(14,6),dpi=600)
sns.barplot(data=avg_rating.head(44),x='brand_name',y='avg_rating',palette='cool',width=.4)
plt.xlabel('brand',color='blue',fontweight='bold',fontsize=20,labelpad=10)
plt.ylabel('avg rating',color='blue',fontweight='bold',fontsize=20,labelpad=10)
plt.title('avg rating for each brand',color='blue',fontweight='bold',fontsize=26)
plt.xticks(rotation=90,fontsize=16)
plt.yticks(fontsize=16)
plt.show()


# In[40]:


plt.figure(figsize=(14,6),dpi=300)
sns.lineplot(data=avg_rating.head(10),x = 'brand_name',y = 'avg_rating',marker = 'D',color='red',palette='winter',markerfacecolor='blue',markersize=10)
plt.title('top 10 brands',color='green',fontweight='bold',fontsize=26)
plt.xlabel('brand',color='blue',fontweight='bold',fontsize=20,labelpad=10)
plt.ylabel('avg rating',color='blue',fontweight='bold',fontsize=20,labelpad=10)
plt.xticks(rotation=90,fontsize=16)
plt.yticks(fontsize=16)
plt.show()


# # 5G vs 4G

# In[60]:


plt.figure(figsize=(14,6),dpi=90)
color=sns.color_palette('summer')
textprops={'color':'black','fontsize':15}
plt.pie(data['5G_or_not'].value_counts(),textprops=textprops,labels=['5G','4G'],colors=color,shadow=True,autopct='%.0f%%',explode=[.2,0])
plt.suptitle('5G or Not',fontsize=20,color='blue')
plt.legend(loc=1)

plt.show()



# # PROCCESSOR VS AVG PRICE

# In[62]:


processes_price = data.groupby('processor_brand')['price'].mean().reset_index()
processes_price = processes_price.sort_values(by='price',ascending=True)
processes_price.head()


# In[66]:


plt.figure(figsize=(16,8),dpi=300)
sns.barplot(data = processes_price,x='processor_brand',y='price',palette='icefire',width=.5)
plt.title('processor according to price',color='blue',fontweight='bold',fontsize=25)
plt.xlabel('processor brand',color='blue',fontweight='bold',fontsize=20,labelpad=10)
plt.ylabel('price',color='blue',fontweight='bold',fontsize=20,labelpad=10)
plt.xticks(rotation=90,color='blue',fontsize=15)
plt.yticks(color='blue',fontsize=15)
plt.show()


# # battery vs price 

# In[74]:


battery_price = data.groupby('battery_capacity')['price'].mean().reset_index()
battery_price = battery_price.sort_values(by='price',ascending=False)
battery_price.head()


# In[80]:


plt.figure(figsize=(14,6),dpi=300)
sns.barplot(data=battery_price.head(20),x = 'battery_capacity',y='price',width=.5,palette='winter',)
plt.title('battery according to price',fontweight='bold',fontsize=25,color='blue')
plt.xlabel('battery capacity',fontweight='bold',fontsize=20,color='blue',labelpad=15)
plt.ylabel('avg price',fontweight='bold',fontsize=20,color='blue',labelpad=15)
plt.xticks(rotation=90,color='green',fontsize=15)
plt.yticks(color='green',fontsize=15)
plt.show()


# In[84]:





# # battery  vs price

# In[87]:


battery_brand=data.groupby('brand_name')['battery_capacity'].max().reset_index()
battery_brand = battery_brand.sort_values(by='battery_capacity',ascending=False)
battery_brand.head()


# In[92]:


plt.figure(figsize=(14,6),dpi=300)
sns.barplot(data=battery_brand,x='brand_name',y='battery_capacity',width=1,palette='icefire',dodge=True)
plt.title('brand according to battery capacity',fontweight='bold',fontsize=25,color='blue')
plt.xlabel('brand name',fontweight='bold',fontsize=20,color='blue',labelpad=15)
plt.ylabel('battery capacity',fontweight='bold',fontsize=20,color='blue',labelpad=15)
plt.xticks(rotation=90,color='green',fontsize=15)
plt.yticks(color='green',fontsize=15)
plt.show()


# # fast charging avilability
# 

# In[96]:


plt.figure(figsize=(14,6),dpi=200)
color_2 =sns.color_palette('winter')

plt.pie(data['fast_charging_available'].value_counts(),labels=['fast charging','non fast'],colors=color_2,autopct='%.0f%%',shadow=True,explode=[.2,1],textprops={'fontweight':'bold','fontsize':12})
plt.title('Fast Charging Availability in Smartphones',fontsize=20)
plt.show()


# #  Number of Rear cameras vs Avg. Price
# 

# In[97]:


number_ofrear=data.groupby('num_rear_cameras')['price'].mean().reset_index()
number_ofrear=number_ofrear.sort_values(by='price',ascending=True)
number_ofrear.head()


# In[104]:


plt.figure(figsize=(14,6),dpi=300)
sns.lineplot(data=number_ofrear.head(20),x='num_rear_cameras',y='price',markerfacecolor='red',markersize=8,marker='D',color='green')
plt.title('number of cameras according to avg price',fontweight='bold',fontsize=25,color='blue')
plt.xlabel('number of cameras',labelpad=10,fontweight='bold',fontsize=20,color='blue')
plt.ylabel('avg price',fontweight='bold',fontsize=20,color='blue',labelpad=10)
plt.xticks(rotation=90,fontsize=15,color='blue')
plt.yticks(fontsize=15,color='blue')
plt.show()


# # Rear camera Resolution vs Avg. Price

# In[105]:


rear_cam_solution=data.groupby('primary_camera_rear')['price'].mean().reset_index()
rear_cam_solution= rear_cam_solution.sort_values(by='price',ascending=True)
rear_cam_solution.head()


# In[107]:


plt.figure(figsize=(14,6),dpi=300)

sns.barplot(data=rear_cam_solution, x='primary_camera_rear',y='price',width=.5,palette='cool')
plt.title('primary cameras according to avg price',fontweight='bold',fontsize=25,color='blue')
plt.xlabel('primary camera',labelpad=10,fontweight='bold',fontsize=20,color='blue')
plt.ylabel('avg price',fontweight='bold',fontsize=20,color='blue',labelpad=10)
plt.xticks(rotation=90,fontsize=15,color='blue')
plt.yticks(fontsize=15,color='blue')
plt.show()


# # Operating System vs Brand 

# In[113]:


plt.figure(figsize=(14,5),dpi=200)
sns.set_style('ticks')
# plot
sns.histplot(data=data,x='brand_name',y='os',binwidth=.3)

# labels
plt.xticks(rotation=90,fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Brand Name',fontsize=20)
plt.ylabel('Operating System',fontsize=20)
plt.title('Operating system used by the brands',fontsize=25)
plt.show()


# In[ ]:




