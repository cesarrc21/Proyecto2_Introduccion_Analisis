#!/usr/bin/env python
# coding: utf-8


#Libraries
import pandas as pd #It helps to better amnipulate data
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn-whitegrid')  #Style for graphs


#Class to better organize the functions created.
class Analyzer():
    def __init__(self,direction,origin,destination,year,product,transport,values):
        self.type = direction
        self.orig = origin
        self.dest = destination
        self.year = year
        self.product = product
        self.transp = transport
        self.vals = values
        
    def bestRoutes(self):  #Function to get the 10 most used routes
        routes = {} 
        r_values = {}
        for route in zip(self.orig,self.dest):
            if route not in routes.keys(): routes[route] = 1
            else: routes[route] += 1
            
        #Sorting routes and taking 10 best according to their frecuency
        total_routes = {k:v for k,v in sorted(routes.items(), key=lambda x:x[1], reverse=True)[0:10]}
        
        for i in range(len(self.vals)): #Getting incomes per routes
            if (self.orig[i],self.dest[i]) in total_routes.keys():
                if (self.orig[i],self.dest[i]) not in r_values.keys():
                    r_values[(self.orig[i],self.dest[i])] = self.vals[i]
                else: r_values[(self.orig[i],self.dest[i])] += self.vals[i]
            else: continue
            
        fig,ax = plt.subplots(figsize=(8,4))  #Plotting 10 best routes vs their frecuencies
        keys = np.arange(len(total_routes.keys()))  
        plt.bar(keys,total_routes.values(),color='navy')
        plt.ylabel('Frecuency', fontweight='bold',fontsize=11,style='italic')
        labels = list(total_routes.keys())
        plt.xticks(keys,labels, rotation=90,fontweight='bold')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        
        fig, ax1 = plt.subplots(figsize=(8,4))  #Plotting 10 best routes vs their incomes
        keys2 = np.arange(len(r_values.keys())) #arange take int values instead tuples to can plot the bar chart 
        plt.bar(keys2,r_values.values(),color='darkgoldenrod')
        plt.ylabel('Incomes', fontweight='bold',fontsize=11,style='italic')
        labels2 = list(r_values.keys())  #then tuples are taken as strings to put them as ticks in x label
        plt.xticks(keys2,labels2,rotation=90,fontweight='bold')
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        
        return print("\n ////Best Routes/////")
    
    
    def Transports(self):  #Function to get how frecuent transports are used and their incomes
        exp_trans = {}
        imp_trans = {}
        for i in range(len(self.transp)):
            if self.type[i] == 'Exports':
                if self.transp[i] not in exp_trans.keys():
                    exp_trans[self.transp[i]] = self.vals[i]
                else: exp_trans[self.transp[i]] += self.vals[i]
            elif self.type[i] == 'Imports':
                if self.transp[i] not in imp_trans.keys():
                    imp_trans[self.transp[i]] =self.vals[i]
                else: imp_trans[self.transp[i]] += self.vals[i]
            else:
                continue
        
        fig, ax = plt.subplots(figsize=(7,5))  #Plotting transports' frecuancy
        df.groupby(self.transp).size().plot.bar(color='k',alpha=0.9)
        plt.ylabel('Frecuency', fontweight='bold',fontsize=11,style='italic')
        plt.xlabel(' ')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        fig,ax1 = plt.subplots(figsize=(7,5))  #Plotting transports' incomes
        plt.bar(*zip(*exp_trans.items()),alpha =0.6,label='Exports',color='teal')
        plt.bar(*zip(*imp_trans.items()),label='Imports',color='darkorange')
        plt.ylabel('Incomes',fontweight='bold',style='italic',fontsize=11)
        plt.xticks(fontweight='bold')
        plt.legend()
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        
        return print("\n ////Transports/////")
        
        
    def Incomes(self):  # Function to get incomes generated per country,year and products 
        countries_incomes = {}
        count = 0
        eighty_percent = sum(self.vals)*.80
        for country,income in zip(self.orig,self.vals):
            if country not in countries_incomes.keys():
                countries_incomes[country] = income
            else:
                countries_incomes[country] += income
                
        #Sorting countries by the incomes they generate        
        order = sorted(countries_incomes.items(), key=lambda item: item[1],reverse=True) 
        total_incomes={}
        for k, v in order:
            if count < eighty_percent:
                count += v
                total_incomes[k] = v
            else: break
                
        fig,ax = plt.subplots(figsize=(8,4))  #Plotting countries vs their incomes
        plt.bar(*zip(*total_incomes.items()),color='darkgreen')
        plt.xticks(rotation=90)
        plt.ylabel('Total_incomes', fontweight='bold',style='italic',fontsize=11)
        plt.xticks(fontweight='bold')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        
        years = {}
        products = {}
        for i in range(len(df.total_value)):
            if self.year[i] not in years.keys():
                years[self.year[i]] = self.vals[i]
            else:  years[self.year[i]] += self.vals[i]

            if self.product[i] not in products.keys():
                products[self.product[i]] = self.vals[i]
            else: products[self.product[i]] += self.vals[i] 
        
        fig, ax1 = plt.subplots(figsize=(8,4)) #Ploting years vs their incomes generated
        plt.bar(*zip(*years.items()),color='olive')
        plt.ylabel('Income',fontweight='bold',style='italic',fontsize=11)
        plt.xticks(fontweight='bold')
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        
        fig, ax2 = plt.subplots(figsize=(14,4)) #Plotting products vs their incomes
        plt.bar(*zip(*products.items()),color='forestgreen',alpha=0.95)
        plt.xticks(rotation=90,fontweight='bold')
        plt.ylabel('Income',fontweight='bold',style='italic',fontsize=11)
        ax2.spines['right'].set_visible(False)
        ax2.spines['top'].set_visible(False)

        return print("\n ////Incomes/////")
           
        
    def yearFacts(self, y):  #Function to get facts about a specific year
        data = {}
        data['routes'] = {}
        data['products'] = {}
        data['transports'] = {}
        for i in range(len(self.year)):
            if self.year[i] == y:
                if (self.orig[i],self.dest[i]) not in data['routes']:
                    data['routes'][(self.orig[i],self.dest[i])] = self.vals[i]
                else: 
                    data['routes'][(self.orig[i],self.dest[i])] += self.vals[i]
                
                if self.product[i] not in data['products']:
                    data['products'][self.product[i]] = self.vals[i]
                else: 
                    data['products'][self.product[i]] += self.vals[i]
                    
                if self.transp[i] not in data['transports']:
                    data['transports'][self.transp[i]] = self.vals[i]
                else: 
                    data['transports'][self.transp[i]] += self.vals[i]     
            else: continue
                
        #Sorting routes, products and transports by their incomes 
        best_routes = {k:v for k,v in sorted(data['routes'].items(), key=lambda x:x[1], reverse=True)[0:5]}
        best_products = {k:v for k,v in sorted(data['products'].items(), key=lambda x:x[1], reverse=True)[0:5]}
        best_transports = {k:v for k,v in sorted(data['transports'].items(), key=lambda x:x[1], reverse=True)[0:5]}
        
        fig,ax = plt.subplots(figsize=(7,5))  #Plotting routes' incomes
        keys3 = np.arange(len(best_routes.keys()))
        plt.bar(keys3,best_routes.values(),color='navy')
        plt.ylabel('Income',fontweight='bold',style='italic',fontsize=11)
        labels3 = list(best_routes.keys())
        plt.xticks(keys3,labels3,rotation=90,fontweight='bold')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        
        fig,ax1 = plt.subplots(figsize=(7,5))  #Plotting products' incomes
        plt.bar(*zip(*best_products.items()),color='darkslategrey')
        plt.ylabel('Income',fontweight='bold',style='italic',fontsize=11)
        plt.xticks(rotation = 90,fontweight='bold')
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        
        fig,ax2 = plt.subplots(figsize=(7,5))  #Plotting transports' incomes
        plt.bar(*zip(*best_transports.items()),color='darkcyan')
        plt.ylabel('Income',fontweight='bold',style='italic',fontsize=11)
        plt.xticks(fontweight='bold')
        ax2.spines['right'].set_visible(False)
        ax2.spines['top'].set_visible(False)
                
        return print("\n ////Facts/////") 




#Using pandas to read csv file as dataframe. This lib to an ease use of attr. 
df = pd.read_csv('synergy_logistics_database.csv',sep=",")



#Calling to the class Analyzer with arg of direction, origin, year, product, transport and values respectively.
Synergy = Analyzer(df['direction'],df['origin'],df['destination'],df['year'],df['product'],
                   df['transport_mode'],df['total_value'])


#Calling bestRoutes function
Synergy.bestRoutes()


#Calling Transports function
Synergy.Transports()


#Calling Incomes function
Synergy.Incomes()


#Calling yearFacts function
Synergy.yearFacts(2019)


Synergy.yearFacts(2020)

