(.index+.total) as $sum_val
| .
|= . + {sum_val: $sum_val}
| select(.sum_val>1.99)
