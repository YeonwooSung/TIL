// 1. Inline when possible!

const array = [1, 2, 3];

/* This is not good... */
array.map((number) => {
    return number * 2;
});

/* This is better */
array.map(number => number * 2);

// When the function has one expression, a good practice is to inline the arrow function!


// 2. Try to distinguish clearly the fat arrow from the comparison operator!

// a) use parenthesis (the easiest way)
const negativeToZero_Bad = number => number <= 0 ? 0 : number;
const negativeToZero_Good = number => (number <= 0 ? 0 : number);

// b) deliberatively define the arrow function using a longer form
const negativeToZero_Good2 = number => {
    return number <= 0 ? 0 : number;
};

// If the arrow function contains the operators >, <, <=, and >=, a good practice is to wrap the expression into a pair of parentheses 
// or deliberately use a longer arrow function form.
