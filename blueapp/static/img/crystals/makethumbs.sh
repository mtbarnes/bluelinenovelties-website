mkdir thumb
for i in *.jpg; do
  convert $i -resize 780 thumb/$i
done

