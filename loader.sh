#load file
echo "enter file to load"
read file
if [ -f "$file" ]; then
echo "file exists"
else
echo "file does not exist"
fi