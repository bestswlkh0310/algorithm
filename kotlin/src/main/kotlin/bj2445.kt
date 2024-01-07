fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        for (j in 0 .. i) {
            print("*")
        }
        for (j in i * 2 until (n - 1) * 2) {
            print(" ")
        }
        for (j in 0 .. i) {
            print("*")
        }
        println()
    }
    for (i in 0 until n - 1) {
        for (j in i until n - 1) {
            print("*")
        }
        for (j in 0 until (i + 1) * 2){
            print(" ")
        }
        for (j in i until n - 1) {4
            print("*")
        }
        println()
    }
}

//*        *
//**      **
//***    ***
//****  ****
//**********

//****  ****
//***    ***
//**      **
//*        *

//5