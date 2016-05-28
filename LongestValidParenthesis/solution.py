def longest_valid_parentheses(s)
  stack = []
  counter = 0
  largest = 0
  s.each_char do |c|
    if c == '('
      stack.push(c)
      next
    end
    popped = stack.pop() if c == ')'
    if popped == '('
      counter = counter + 2
    else
      counter = 0
      stack = []
    end
    largest = counter if counter > largest
  end
  if stack.empty?
    largest
  else
    stack
  end
end

  # iterate through s
  # push onto stack on (
  # pop off of stack on )
  # if attempting to pop empty stack, reset counter
  # otherwise increment counter
  # have a largest var to store counter

  # got to this point and realized its not as simple as a stack, its a dyn prog problem. 
  # thought of the case ()(((((((((((((((((((), a simple stack implementation cannot know that there are no closing parens
  # and so this will return 4 even though the longest valid substring is only ().