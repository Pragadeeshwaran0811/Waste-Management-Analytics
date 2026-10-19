import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


df= pd.read_csv(r"C:\Users\praga\Downloads\Waste_Management_and_Recycling_India (1).csv")
df.head()


# In[4]:


df.shape


# In[5]:


df.columns


# In[9]:


df.info()


# In[15]:


df["Waste Generated (Tons/Day)"].mean()


# In[16]:


df["Waste Generated (Tons/Day)"].sum()


# In[18]:


df["Waste Generated (Tons/Day)"].max()


# In[19]:


df["Waste Generated (Tons/Day)"].min()


# In[20]:


df.describe()


# In[22]:


df["Waste Type"].value_counts()


# In[24]:


df["Disposal Method"].value_counts()


# In[25]:


df["Year"].value_counts()


# In[27]:


df.groupby("Waste Type")["Waste Generated (Tons/Day)"].sum()


# In[28]:


df.groupby("Waste Type")["Recycling Rate (%)"].mean()


# In[29]:


df.groupby("Year")["Waste Generated (Tons/Day)"].sum()


# In[30]:


df.groupby("Year")["Recycling Rate (%)"].mean()


# In[5]:


df["Municipal Efficiency Score (1-10)"].corr(df["Recycling Rate (%)"])


# In[7]:


df.groupby("Waste Type")["Waste Generated (Tons/Day)"].mean()


# In[8]:


df.groupby("Waste Type")["Cost of Waste Management (₹/Ton)"].mean()


# In[10]:


df.groupby("Waste Type")[["Cost of Waste Management (₹/Ton)","Waste Generated (Tons/Day)"]].max()


# In[16]:


df.groupby("City/District")["Waste Generated (Tons/Day)"].sum().sort_values(ascending=False).head()


# In[17]:


df.groupby("Disposal Method")["Recycling Rate (%)"].mean()


# In[18]:


df.groupby("Disposal Method")["Recycling Rate (%)"].max()


# In[19]:


df.groupby("Disposal Method")["Recycling Rate (%)"].min()


# In[26]:


plt.scatter(df["Population Density (People/km²)"],df["Waste Generated (Tons/Day)"])
plt.xlabel("Population Density (People/km²)")
plt.ylabel("Waste Generated (Tons/Day)")
plt.title("Population Density vs Waste Generation")
plt.show()


# In[28]:


df["Population Density (People/km²)"].corr(df["Waste Generated (Tons/Day)"])


# In[29]:


plt.scatter(df["Awareness Campaigns Count"],df["Recycling Rate (%)"])
plt.xlabel("Awareness Campaigns Count")
plt.ylabel("Recycling Rate (%)")
plt.title("Awareness Campaigns vs Recycling Rate")
plt.show()


# In[30]:


df["Awareness Campaigns Count"].corr(df["Recycling Rate (%)"])


# In[33]:


df.groupby("City/District")["Recycling Rate (%)"].mean().sort_values(ascending=False).head()


# In[34]:


df.groupby("City/District")["Municipal Efficiency Score (1-10)"].mean().sort_values(ascending=False).head()


# In[35]:


plt.scatter(df["Municipal Efficiency Score (1-10)"],df["Recycling Rate (%)"])
plt.xlabel("Municipal Efficiency Score (1-10)")
plt.ylabel("Recycling Rate (%)")
plt.title("Municipal Efficiency Score vs Recycling Rate")
plt.show()


# In[39]:


df.groupby("Disposal Method")["Cost of Waste Management (₹/Ton)"].mean().sort_values(ascending=False)


# In[42]:


df.groupby("Disposal Method")["Waste Generated (Tons/Day)"].sum().sort_values(ascending=False)


# In[44]:


plt.scatter(df["Landfill Capacity (Tons)"],df["Waste Generated (Tons/Day)"])
plt.xlabel("Landfill Capacity(Tons)")
plt.ylabel("Waste Generated (Tons/Day)")
plt.title("Landfill Capacity vs Waste Generation")
plt.show()


# In[45]:


df["Landfill Capacity (Tons)"].corr(df["Waste Generated (Tons/Day)"])


# In[46]:


city_analysis = df.groupby("City/District").agg(
    Total_Waste=("Waste Generated (Tons/Day)", "sum"),
    Avg_Recycling_Rate=("Recycling Rate (%)", "mean")
).sort_values("Total_Waste", ascending=False).head(5)

city_analysis


# In[ ]:




