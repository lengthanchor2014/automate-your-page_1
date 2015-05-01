'''

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Chapter 2 - Crate HTML document
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Psuedo Code for my Program 

#1 - nested_list 

Created an Input function called "nested_list" that houses the values that I want to use in my HTML document.

Note: There are a total of 4 list with 2 values per list. 






#2 - while_program (p) 

"while_program" then calls for variable "nested_loop" values. 





#3 - While Loop Executes

"while_program" then executes to extracts and seperate my values in "nested_loop" by using  funciton while loop steps through the values. 

Note:

Example: First Loop example
	
i= 0, starts at 0 because when grabing the information form nest_loop it starts at 0
n = len(p) = 4, tells the  number of list in  the program  (p = nest_loop = 4)

while 0<4: (while loop is true as since 4 is greater than 0)
				
    a = p[0]                        #  a = p[0] = save first list value in nest_loop list = [Title: HTML , Description: Hypertext Markup Language forms the structure of webpages],
	title =  a[0]                   #  title  = extract the title string = Title:HTML , grab the string value 
	description =  a[1]             #  description = estract strin = Description: Hypertext Markup Language forms the structure of webpages
    concept = title + description  #  concept = concatinaiotn of two string = Title:HTML Description: Hypertext Markup Language forms the structure of webpages








#4 - Small program within "while_program" 

A Small program exectures to extract informaiton for HTML: 
	
	
		Ex - Continue with first while loop: 
			
        #5.def get_title(concept):         ---> finds title information and stores it in the variable called  "title" 
                                           ---> title  = HTML Description

		#6. def get_description(concept):  ---> finds title description information and stores it in the variable "description"
		                                   ---> description = Hypertext Markup Language forms the structure of webpages
		
        #7. get_description(concept):      ---> uses the "title" and "description" information to populate through out our HTML document 
										    --->  prints of the html code using variable "title" and "description" to populate the HTML Code
										    <div class="concept">
											  												  	       <div class="concept-title">
											
											  													          HTML 
											  													       </div>
											
											  												  	       <div class="concept-description">
											
											  													       Hypertext Markup Language forms the structure of webpages
											  													       </div>
											  </div>
										




#8 - Order repeated in the while loop. 

The order is repeated with, i=i+1" keeping track the next count for the next loop of html informaiton.  

'''


#3. While loop executes

def while_program (p): 
	i = 0
	n = len(p)  # = number elements which is 4
	
	while i< n:
		   
			a = p[i]
			
			
			title =  a[0]
			description =  a[1]
			
			concept = title + description
			
			
			
			#4.  Small program within "while_program"
			#####################################################################
			title = get_title(concept)
			description = get_description(concept)
			concept_html = generate_concept_HTML(title, description)
			
			#####################################################################
						
			
			#8.  Order repeated and keeps counts 
			i=i+1
			

#5. Small Program - get_title, gets title from concept vairable 
def get_title(concept):
	start = concept.find("Title:")
	end = concept.find("Description:")
	title = concept [start+7: end]
	return  title
	
#6.	Small Program - get_description, gets description from concept vairable
def get_description(concept):
	start_1 = concept.find('Description: ')
	description = concept[start_1 +13: ]
	return   description
	
#7.Small Program - generate_concept_HTM , gets title & description and outputs there values in my HTML document. 
def generate_concept_HTML(title, description):
		
	
	  html_1 = '''
	  <div class="concept">
	  						<div class="concept-title">
	
	  						''' + title

	  html_2 = '''
	  						</div>
	
	  						<div class="concept-description">
	
	  						''' + description

	  html_3 = '''
	  						</div>
	  </div>'''

	  html_all = html_1 + html_2 + html_3
	  print html_all


#  1. Input 
	
nested_list = [
			    ['Title: HTML ', 'Description: Hypertext Markup Language forms the structure of webpages'],
                ['Title: CSS ' , 'Description: Cascading Style Sheets give pages style'],
                ['Title: Python ', 'Description: Python is a programming language'],
                ['Title: Lists ', 'Description: Lists are a data structure that let you organize information']
              ]


# 2. call program "while_program"  & "nested_list" variable
while_program (nested_list)

