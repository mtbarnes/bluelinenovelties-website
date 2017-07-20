mkdir thumb
for i in *.jpg; do
  convert $i -chop 700x500 thumb/$i
done

