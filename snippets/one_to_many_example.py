___author___ = "dgutman"

#Code Snippet 4: Complex Case: Many to One Relationship

FAS_vars = { 'map_type' : 'complex', 'var_dict': {
  'fas_f_1': ['B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18'],
  'fas_f_2': ['B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25'],
  'fas_f_3': ['B26', 'B27', 'B28', 'B29', 'B30', 'B31', 'B32', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32'],
  'fas_f_4': ['B33', 'B34', 'B35', 'B36', 'B37', 'B38', 'B39', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39'],
  'fas_f_tot': ['B40']} }



##In this example the words associated with the letter F appear in up to 10 fields for each 15-second block
##Since I didn't want to create 60 variables to store the F data in my RCP Project, the following code 
## Grabbed these cells as a block and merged them into a single string

