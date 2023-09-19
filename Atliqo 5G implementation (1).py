#!/usr/bin/env python
# coding: utf-8

# # AtlioQo Telecom 
# **Fictional Company:**
# 
# *AtliQo is one of the leading telecom providers in India and launched it’s 5G plans in May 2022 along with other telecom providers.*
# 
# **However, the management noticed a decline in their active users and revenue growth post 5G launch in May 2022.** 
# 
# * Atliqo’s business director requested their analytics team to provide a comparison report of KPIs between pre and post-periods of the 5G launch. 
# * The management is keen to compare the performance between these periods and get insights which would enable them to make informed decisions to recover their active user rate and other key metrics. 
# * They also wonder if they can optimize their internet plans to get more active users.  Peter Pandey, a junior data analyst is assigned to this task.
# 

# # Data Set: atlioqo-telecom-dataset
# **1. fact_atliqo_metrics**
# **Column Description for fact_atliqo_metrics:**
# 1. date: This column represents the starting date of each month.
# 2. city_code: This column represents the unique pincode code given for each city.
# 3. company: This column represents the company name for which the data is provided. In this dataset it's only Atliqo. 
# 4. atliqo_revenue_crores: This column represents the revenue that Atliqo got on that particular month in that city_code in crores(unit of currency in India - 1Crore = 10 Million) from the internet users. 
# 5. arpu: This column represents the average revenue per user. That means on average how much revenue Atliqo generated on single user for a given time period.
# 6. active_users_lakhs: This column represents the number of active users who are using Atliqo's service on that particular month in that city_code in lakhs(unit of currency in India - 1 Lakh = 100,000).
# 7. unsubscribed_users_lakhs: This column represents the number of unsubscribed users who unsubscribed from Atliqo on that particular month in that city_code in lakhs(unit of currency in India - 1 Lakh = 100,000). 
# 
# **2. fact_market_share**
# **Column Description for fact_market_share:**
# 1. date: This column represents the starting date of each month.
# 2. city_code: This column represents the unique code given for each city.
# 3. tmv_city_crores: This column represents the total market value of the city in that month in crores(unit of currency in India) from the internet users. 
# 4. company: This column represents the different competitor names in the telecom industry [Atliqo, Britel, DADAFONE, PIO, Others].
# 5. ms_pct: This column represents the percentage of market share gained by respective company from the total market value(tmv_city) on that particular month in that city-code. 
# 
# **3. fact_plan_revenue**
# **Column Description for fact_plan_revenue:**
# 1. date: This column represents the starting date of each month.
# 2. city_code: This column represents the unique code given for each city.
# 3. plans: This column represents the various internet plans provided by the Atliqo company to the users.
# 4. plan_revenue_crores: This column represents the revenue that Atliqo got from that respective plan on that particular month in that city_code in crores (unit of currency in India - 1Crore = 10 Million).
# 
# 

# In[1]:


# import library
import numpy as np
import pandas as pd
import os
from matplotlib import pylab as plt


# In[2]:


# import the excel file for analysis
fam=pd.read_excel(r"C:\Users\tusha\Desktop\Project\C3 Input_for_Participants/data_set.xlsx",sheet_name="fact_atliqo_metrics")
fms=pd.read_excel(r"C:\Users\tusha\Desktop\Project\C3 Input_for_Participants/data_set.xlsx",sheet_name="fact_market_share")
fpr=pd.read_excel(r"C:\Users\tusha\Desktop\Project\C3 Input_for_Participants/data_set.xlsx",sheet_name="fact_plan_revenue")


# In[3]:


fam.head() # Data inside fact_atliqo_metrics file


# In[4]:


fam.info() # column details


# In[5]:


fam.isnull().sum() # data is cosistant with no null value


# In[6]:


print("Total Revenue is "+str(fam['atliqo_revenue_crores'].sum())+" crores.")


# In[7]:


print("Avg. Revenue is "+str(fam['atliqo_revenue_crores'].sum()/8)+" crores.")


# # Spliting the Revenue based on Before and After 5G implementation
# * First 4 months of 2022 are showing the revenue Before 5G implementation.
# * After 4 months of 2022 are showing the revenue After 5G implementation.

# In[8]:


df=fam.groupby(by='before/after_5g')
fam_before_5G = df.get_group('Before 5G')
fam_after_5G = df.get_group('After 5G')


# In[9]:


fam_before_5G.head() 


# In[10]:


fam_after_5G.head()


# In[11]:


print("Before 5G")
print("Total Revenue is "+str(fam_before_5G['atliqo_revenue_crores'].sum())+" crores.")
print("Avg. Revenue is "+str(round(fam_before_5G['atliqo_revenue_crores'].sum()/4,2))+" crores.")


# In[12]:


print("After 5G")
print("Total Revenue is "+str(round(fam_after_5G['atliqo_revenue_crores'].sum(),2))+" crores.")
print("Avg. Revenue is "+str(round(fam_after_5G['atliqo_revenue_crores'].sum()/4,2))+" crores.")


# In[13]:


print("Average Revenue Per User before 5G 'arpu' " + str(round(fam_before_5G['arpu'].mean(),2)))
print("Average Revenue Per User after 5G 'arpu' " + str(round(fam_after_5G['arpu'].mean(),2)))
print("arpu increaseed by " + str(round((fam_after_5G['arpu'].mean()-fam_before_5G['arpu'].mean()),2)))


# In[14]:


print("Total Active user before 5G " + str(round(fam_before_5G['active_users_lakhs'].sum(),2))+" lakhs.")
print("Total Active user after 5G " + str(round(fam_after_5G['active_users_lakhs'].sum(),2))+" lakhs.")
print("Reduction in total active user after 5G " + str(round((fam_before_5G['active_users_lakhs'].sum()-fam_after_5G['active_users_lakhs'].sum()),2))+" lakhs.")


# In[15]:


print("Total unsubscribed users before 5G " + str(round(fam_before_5G['unsubscribed_users_lakhs'].sum(),2))+" lakhs.")
print("Total unsubscribed users after 5G " + str(round(fam_after_5G['unsubscribed_users_lakhs'].sum(),2))+" lakhs.")
print("Increase in unsubscription after 5G " + str(round((fam_after_5G['unsubscribed_users_lakhs'].sum())-fam_before_5G['unsubscribed_users_lakhs'].sum(),2))+" lakhs.")


# In[16]:


fam.head()


# In[17]:


Atliqo=fam.groupby('month_name',as_index = False,sort=False).sum()
Atliqo_m=fam.groupby('month_name',as_index = False,sort=False).mean()


# In[18]:


Atliqo.head()


# In[19]:


for i in range(0,8):
    print("In month of {} Atliqo Revenue {} crores having Average Revenue Per User {}. Active user {} lakhs where as unsubscribed user become {} lakhs.".format(str(Atliqo.loc[i,'month_name']),str(Atliqo.loc[i,'atliqo_revenue_crores']),str(round(Atliqo_m.loc[i,'arpu'],2)),str(Atliqo.loc[i,'active_users_lakhs']),str(Atliqo.loc[i,'unsubscribed_users_lakhs'])))


# In[20]:


fig,ax=plt.subplots(1,3,figsize = (16,9),dpi=300)
ax[0].set_title("Active Users in lakhs vs Month")
ax[0].set_xlabel('Month')
ax[0].set_ylabel('Users in lakhs')
ax[0].plot(Atliqo['month_name'],Atliqo['active_users_lakhs'],marker='*',markersize = 10,markerfacecolor = "white")
ax[1].set_title("Unsubscribed Users in lakhs")
ax[1].set_xlabel('Month')
ax[1].set_ylabel('Users in lakhs')
ax[1].plot(Atliqo['month_name'],Atliqo['unsubscribed_users_lakhs'],marker='o',markersize = 10,markerfacecolor = "white")
ax[2].set_title("Average Revenue Per User over all city")
ax[2].set_xlabel('Month')
ax[2].set_ylabel('Average Revenue Per User')
ax[2].plot(Atliqo['month_name'],Atliqo_m['arpu'],marker='s',markersize = 10,markerfacecolor = "white")


# In[21]:


fms.head()


# In[22]:


fms["company"].unique()


# In[23]:


fms.groupby('company').sum()


# In[24]:


f=fms.groupby(by='company')
fam_before_5G = df.get_group('Before 5G')
fam_after_5G = df.get_group('After 5G')


# In[25]:


f_Atliqo = f.get_group('Atliqo')
f_Britel = f.get_group('Britel')
f_PIO = f.get_group('PIO')
f_DADAFONE = f.get_group('DADAFONE')
f_Others = f.get_group('Others')


# In[26]:


f_Atliqo.head()


# In[27]:


a=f_Atliqo.groupby('month_name',as_index = False,sort=False).mean()
b=f_Britel.groupby('month_name',as_index = False,sort=False).mean()
c=f_PIO.groupby('month_name',as_index = False,sort=False).mean()
d=f_DADAFONE.groupby('month_name',as_index = False,sort=False).mean()
e=f_Others.groupby('month_name',as_index = False,sort=False).mean()


# In[28]:


fig,ax=plt.subplots(dpi=200)
ax.set_title("Market Share %")
ax.set_xlabel('Month name')
ax.set_ylabel('Average of Market share')
ax.plot(a['month_name'],a['ms_pct'],marker='*',markersize = 10,markerfacecolor = "white")
ax.plot(b['month_name'],b['ms_pct'])
ax.plot(c['month_name'],c['ms_pct'])
ax.plot(d['month_name'],d['ms_pct'])
ax.plot(e['month_name'],e['ms_pct'])
ax.legend(['Atliqo', 'Britel', 'PIO', 'DADAFONE', 'Others'],loc=2)


# In[29]:


f=f_Atliqo.groupby('city_name',as_index = False,sort=False).sum()
g=f_Britel.groupby('city_name',as_index = False,sort=False).sum()
h=f_PIO.groupby('city_name',as_index = False,sort=False).sum()
i=f_DADAFONE.groupby('city_name',as_index = False,sort=False).sum()
j=f_Others.groupby('city_name',as_index = False,sort=False).sum()


# In[30]:


j


# In[31]:


f['city_name'].unique()


# In[32]:


fig,ax=plt.subplots(figsize = (16,9),dpi=200)
ax.set_title("Market Share %")
ax.set_xlabel('City Name')
ax.set_ylabel('Average of Market share')
ax.bar(f['city_name'],f['ms_pct'],align = 'center',width=0.5,alpha = 0.9)
ax.bar(g['city_name'],g['ms_pct'],align = 'center',width=0.5,alpha =0.7)
ax.bar(h['city_name'],h['ms_pct'],align = 'center',width=0.5,alpha =0.5)
ax.bar(i['city_name'],i['ms_pct'],align = 'center',width=0.5,alpha =0.3)
ax.bar(j['city_name'],j['ms_pct'],align = 'center',width=0.5,alpha =0.1)

ax.legend(['Atliqo', 'Britel', 'PIO', 'DADAFONE', 'Others'],loc=2)


# In[33]:


fpr.head()


# In[34]:


k=fpr.groupby(['before/after_5g','plan_description'],as_index = False,sort='plan_description').sum()


# In[35]:


mask1=k['before/after_5g']=='After 5G'
mask2=k['before/after_5g']=='Before 5G'


# In[36]:


pack=fpr['plan_description'].unique()
bk=k[mask2]
ak=k[mask1]


# In[ ]:





# In[37]:


bk


# In[38]:


for i in range(0,10):
    print("{}) Package: {} \n*. Revenue generated from {} crores before 5g and {} crores after 5G.\n*. The revenue difference {} crores.".format(str(i+1),str(ak.loc[i,'plan_description']),str(bk.loc[(i+10),'plan_revenue_crores']),str(ak.loc[i,'plan_revenue_crores']),str(round(ak.loc[i,'plan_revenue_crores']-bk.loc[(i+10),'plan_revenue_crores'],2))))


# In[ ]:





# In[ ]:





# In[39]:


x=np.linspace(1,13)


# In[40]:


ax = fig.add_axes([0.5,0.1,0.8,0.5])
fig,ax=plt.subplots(figsize=(25,12),dpi=200)
ax.set_title("Plan Revenue")
ax.set_xlabel('Month name')
ax.set_ylabel('Revenue in Crores')
ax.bar(bk['plan_description'],bk['plan_revenue_crores'],align = 'center',width=0.5,alpha = 0.5)
ax.bar(ak['plan_description'],ak['plan_revenue_crores'],align = 'center',width=0.5,alpha = 0.4)
ax.set_xticklabels(pack,rotation=90)
ax.legend(["before 5G",'after 5G'],loc=2)


# In[ ]:





# # Conclusion:
# **There are some facinating insides based on broadband implementation on Before and After 5G implementation:**
# 1. Total Revenue and Average revenue generated in 8 months is 3187.36 crores and 398.42 crores respectively.
# 2. Before 5G: Total Revenue and Average revenue generated is 1597.70 crores and 399.42 crores respectively.
# 3. After 5G: Total Revenue and Average revenue generated is 1589.66 crores and 397.42 crores respectively.
# 4. Active Users: Before 5G 843.53 lakhs and After 5G 773.7 lakhs.
# 5. Unsubscibed Users: Before 5G 56.33 lakhs and After 5G 69.57 lakhs and increase in unsubscribtion is 13.24 lakhs.
# 6. Number of unsubsribtion increase exponentially after 1st month of implementation of 5G.
# 7. The revenue generated from these packages decreases after 5G implementation:
# * 25 GB Combo 3G / 4G Data Pack
# * Mini Ultra Saver Pack (750 MB/Day for 28 Days)
# * Rs. 99 Full Talktime Combo Pack
# * Ultra Duo Data Pack (1.8GB / Day Combo For 55 days )
# * Ultra Fast Mega Pack (3GB / Day Combo For 80 days)
# * Xstream Mobile Data Pack: 15GB Data | 28 days
# 
# **Thus, users from these package shifted from Atliqo to other companies**
# 
# 8. Maket Share graph shows: User from Atliqo switching to PIO after implementation of 5G.
# 

# In[ ]:




