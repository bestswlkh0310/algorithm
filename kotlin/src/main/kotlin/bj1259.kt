fun main() {
    loop@
    while (true) {
        val inp = readln()
        if (inp == "0") break
        for (i in inp.indices) {
            if (inp[i] != inp[inp.length - i - 1]) {
                println("no")
                continue@loop
            }
        }
        println("yes")
    }
}