// Sample Implemantation of IPUT Course IoT Device Programming 3 (2022 Summer)
// Week 11

// Flask Example (33)
// render_template with Python data (list of list) and
// JavaScript example (get_average)

// June 23, 2023
// Michiharu Takemoto (takemoto.development@gmail.com)

// 
// MIT License
// 
// Copyright (c) 2023 Michiharu Takemoto <takemoto.development@gmail.com>
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
// 
// 
// document.write("<br>") ;
// document.write("Start! (JavaScript part!!) in JavaScript file") ;
// document.write("<br>") ;
// document.write("JavaScriptのプログラムコードに引き渡された変数チェック") ;
// document.write("<br>") ;

// for(let i = 0 ; i < global_values.length ; i++) {
//     document.write(global_values[i] + "<br>") ;
// }

let sum_tempe = 0.0 ;
let sum_humid = 0.0 ;
let number_of_data = 0 ;
for(let i = 0 ; i < global_values.length ; i++) {
    let value = global_values[i] ;
    let tempe = parseFloat(value[0]);
    let humid = parseFloat(value[1]);
    sum_tempe = sum_tempe + tempe;
    sum_humid = sum_humid + humid;
    number_of_data = number_of_data + 1 ;
    
}

document.write("------<br>平均<br>") ;
const average_tempe = sum_tempe / number_of_data ;
const average_humid = sum_humid / number_of_data ;

document.write("温度:") ;
document.write(average_tempe) ;
document.write(" 湿度:") ;
document.write(average_humid) ;
document.write(" (データ数:") ;
document.write(number_of_data) ;
//document.write(sum_tempe);
document.write(")<br>") ;

// alert("確認") ;

