const getUniformIntegerCountInInterval = (A, B) => {
  var res = 0
  const numDigitsA = Math.floor(Math.log10(A)) + 1
  const numDigitsB = Math.floor(Math.log10(B)) + 1
  
  for (var digits = numDigitsA; digits <= numDigitsB; digits++) {    
    for (var n = 1; n < 10; n++) {
      const numb = parseInt(String(n).repeat(digits), 10)
      if (numb >= A && numb <= B) res+= 1
    }
  }
  
  return res
}
