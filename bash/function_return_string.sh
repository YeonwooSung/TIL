#!/bin/bash

set -x
function pass_back_a_string() {
    eval "echo in pass_back_a_string, original $1 is \$$1"
    eval "$1='foo bar rab oof'"
}

return_var='original return_var'
pass_back_a_string return_var
echo $return_var

function call_a_string_func() {
     local lvar='original lvar'
     pass_back_a_string lvar
     echo "lvar='$lvar' locally"
}

call_a_string_func
echo "lvar='$lvar' globally"

#----------------------------------------
# Another methods

function getSomeString() {
     echo "tadaa!"
}

return_var=$(getSomeString)
echo $return_var
# Alternative syntax:
return_var=`getSomeString`
echo $return_var
