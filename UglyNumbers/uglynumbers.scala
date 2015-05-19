object Main extends App {
    
    def isUgly(number : Int) : Int = {
        if (number == 0){
            1
        }
        else if (number % 2 == 0){
            1
            
        }
        else if (number % 3 == 0){
            1
        }
        else if (number % 5 == 0){
            1
        }
        else if (number % 7 == 0 ){
            1
        }
        else{
            0
        }
    }
    
    def numUgly(x : Int, y : Int) : Int = {
        (isUgly(x + y) + isUgly(x - y))
    }
      
    def totUgly(total : Int, head : List[Char], tail : List[Char]) : Int = {
        
        def result : Int = tail.toList match {
            case Nil => return numUgly(total, head.mkString.toInt)
            case x::xs => 
            {
                totUgly(total, head:+x,xs) +
                totUgly(total+head.mkString.toInt,List(x),xs) +
                totUgly(total-head.mkString.toInt,List(x),xs)
            }
        }
        result
    }
    
    val source = scala.io.Source.fromFile(args(0))
    val lines = source.getLines.filter(_.length > 0)
    for (l <- lines) {
        val x : List[Char] = l.stripLineEnd.toList
        println(totUgly(0,List(x.head),x.tail)/2)
        
    }
}

