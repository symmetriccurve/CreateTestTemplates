# CreateTestTemplates
Python Script to add test Templates based on type of file.


Add this to the bash script 

```
function addTest {
  a="python temp/create-test-templates/main.py $1 $(pbpaste)"
  echo $a 
  $a
}
```

simply copy the relative path of the file and do

> >addTest component


Above command adds test template for create component
