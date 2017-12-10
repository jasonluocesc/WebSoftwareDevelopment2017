function keywordusage(text, keywords){
  var result = [keywords.length];

  for(i =0;i<keywords.length;i++){
    if (text.indexOf(keywords[i])>-1)
    {
      result[i] = true;
    }
    else{
      result[i] = false;
    }
  }
  return result;
}

function frequencies(text, wordlist){
    var result = {};
    fre = [wordlist.length]

    for(i = 0;i<wordlist.length;i++){
        fre[i] = text.split(wordlist[i]).length-1;
        result[wordlist[i]]=fre[i];
    }
    return result;

}

function rotate(array, steps) {
    var a = [array.length];
    length = array.length;

    if (steps == null) {
        a[0] = array[length - 1];
        for (i = 1; i < length; i++) {
            a[i] = array[i - 1];
        }

    }
    else {
        while (steps<0){
            steps = steps+length;
        }
        if (steps > length) {
            steps = steps % length;
        }
        for (i = 0; i < length; i++) {
            a[(i + steps) % length] = array[i];
        }

        return a;
    }
}