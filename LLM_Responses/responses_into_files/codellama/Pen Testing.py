t, n, c = readline_int_list()
  // The judge secretly picks the number of units for each pen:
  // in test case 1: 2 0 4 1 3
  // in test case 2: 1 3 2 4 0
  // We write with the 4-th pen in test case 1, and with the 5-th pen in test case 2.
  printline 4 5 to stdout
  flush stdout
  // Reads 1 0, as the 4-th pen in test case 1 still had ink left,
  // but the 5-th pen in test case 2 did not.
  a1, a2 = readline_int_list()
  // We write with the 4-th pen in test case 1 again, and with the 3-rd pen in test case 2.
  printline 4 3 to stdout
  flush stdout
  // Reads 0 1.
  a1, a2 = readline_int_list()
  // We only write in test case 2 this time, with the 2-nd pen.
  printline 0 2 to stdout
  flush stdout
  // Reads 0 1.
  a1, a2 = readline_int_list()
  // We decide we are ready to answer.
  printline 0 0 to stdout
  flush stdout
  // We take the 3-rd and the 4-th pens to the South Pole in both test cases.
  printline 3 4 3 4 to stdout
  flush stdout
  // In test case 1, the remaining amounts in the 3-rd and the 4-th pens are 4 and 0, and 4+0<5,
  // so we did not succeed.
  // In test case 2, the remaining amounts in the 3-rd and the 4-th pens are 1 and 4, and 1+4≥5,
  // so we succeeded.
  // We have succeeded in 1 out of 2 test cases, which is good enough since c=1.
  exit