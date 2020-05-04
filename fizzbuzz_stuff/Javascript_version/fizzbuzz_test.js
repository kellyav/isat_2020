// ES2015 and before:
    // const someFunction = reqquire('./theFiletoImportitFrom)
// ES2016 and after:
    // import someFunction from './theFiletoImportitFrom
    // export const thingtobeExported= // definition of thing goes here 

// import the code to be tested 
const  fizz = require('..fb_js/fizzbuzz')

describe('A FizzBuzz program', () => {
    it('has a smoke test', () => {
        expect(true).toBe(true)
        expect(false.not.toBe(true)
    })
    
    describe('A function fizz()', () => {
        it('throws an error if it has no input', () => {
        expect() => {fizz()}.toThrow('there is no input')
        })
    })
    })


// npm test 