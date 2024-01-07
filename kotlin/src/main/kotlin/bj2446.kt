fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        for (j in 0 until i) {
            print(" ")
        }
        for (j in i * 2 .. (n - 1) * 2) {
            print("*")
        }
        println()
    }
    for (i in 0 until n - 1) {
        for (j in i until n - 2) {
            print(" ")
        }
        for (j in 0 .. (i + 1) * 2){
            print("*")
        }
        println()
    }
}

//*********
// *******
//  *****
//   ***
//    *
//   ***
//  *****
// *******
//*********

//5