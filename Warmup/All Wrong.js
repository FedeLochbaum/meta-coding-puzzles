const op = { 'A': 'B', 'B': 'A' }

const getWrongAnswers = (N, C) => Array.from(C).reduce((acc, letter) => acc + op[letter], '')
