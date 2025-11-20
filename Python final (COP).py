plus_minus_symbol = "\u00B1" #Got this from Google
print("World's Best Calculator, here you can have all and every formula needed for math classes so you don't have to worry about memorizing them anymore!\n")
print("*Small note: if you wish to end the program, use CTRL + C*\n")

while True:
    print("\n\nPick 1 for Algebra \nPick 2 for Geometry \nPick 3 for Pre-Calculus \n")
    choice=input("Select 1, 2 or 3: ")
    if choice=="1": #Algebra
        print("\nWelcome to Algebra! \nPick 1 for formulas \nPick 2 for solutions\n")
        option=input("Select 1 or 2: ")
        if option=="1": #Formulas
            print("\nPick 1 for Forms of Linear Equations \nPick 2 for Forms of Quadratic Functions \nPick 3 Forms of Exponential Functions"
                  "\nPick 4 for Quadratic Formula \nPick 5 Final Amounts under Simple Interest \nPick 6 for Final Amounts under Compound Interest\n")
            formulas=input("Select 1,2,3,4,5 or 6: ")
            if formulas=="1":#1. linear equations
                print("Forms of Linear Equations are: \n\nSlope Intercept form: \ny=mx+b \n\nStandard form: \nAx+By=C \n\nPoint-Slope Formula: \ny-y1=m(x-x1)\n")
            elif formulas=="2":#2. Quadratic equations
                print("Forms of Quadratic Functions are: \n\nStandard form: \nf(x)= ax^+bx+c \n\nCompleted-square form: \nf(x)= a(x-h)^2+k \n\n"
                      "How to complete the square: \n(b/2a)^2 \n\nFactored form: \nf(x)= a(x-p)(x-q)")
            elif formulas=="3": #3. exponential functions
                print("Forms of Exponential Functions are: \n\nParent function: \nf(x)= ab^x \n\nexponential growth/decay: \nf(x)= a(1" +plus_minus_symbol+ "r)^x")
            elif formulas=="4": #4. quadratic formula
                print("Quadratic formula: \nx= -b" +plus_minus_symbol+ "(√b^2-4ac)/2a")
            elif formulas=="5": #5. simple interest
                print("Final amounts under Simple Interest: \nA=P(1+rt), where P= principal, r= rate, and t= time")
            elif formulas=="6": #6. compound interest
                print("Final Amounts under Compound Interest: \nA=P=(1+r/n)^nt, where P= principal, r= rate, n= number of times compounded, and t= time")
            else:
                print("Invalid choice!")
        elif option=="2": #solutions
            print("\nPick 1 for Forms of Linear Equations \nPick 2 for Forms of Quadratic Functions \nPick 3 Forms of Exponential Functions"
                  "Pick 4 for Quadratic Formula \nPick 5 Final Amounts under Simple Interest \nPick 6 for Final Amounts under Compound Interest\n")
            solutions=input("Select 1,2,3,4,5 or 6: ")
            if solutions=="1": #1. linear equations
                print("Pick 1 for slope \nPick 2 for slope intercept form \nPick 3 for Point Slope Formula")
                linear=input("Select 1,2, or 3: ")
                if linear=="1": #1.1 slope
                    print("Slope formula: m=(y2-y1)/(x2-x1)")
                    print()
                    y1=int(input("Enter your 'Y1' value: "))
                    y2=int(input("Enter your 'Y2' value: "))
                    x1=int(input("Enter your 'X1' value: "))
                    x2=int(input("Enter your 'X2' value: "))
                    slope=(y2-y1)/(x2-x1)
                    print()
                    print(f'Your slope is: m= {slope:.2f}')
                elif linear=="2": #1.2 slope intercept
                    print("Slope Intercept form: y=mx+b")
                    print()
                    m=int(input("Enter your slope: "))
                    b=int(input("Enter your y-intercept: "))
                    print()
                    print(f"Your slope intercept form formula is: y={m}x+{b}")
                elif linear=="3": #1.3 point-slope
                    print("Point-slope formula: y-y1=m(x-x1)")
                    print()
                    x1=int(input("Enter your X1 value: "))
                    y1=int(input("Enter your Y1 value: "))
                    m=int(input("Enter your slope: "))
                    if m>0 and y1>0 and x1>0:
                        point_slope=m*(-x1)+y1
                    elif m>0 and y1>0 and x1<0:
                        point_slope=m*x1+y1
                    elif m>0 and y1>0 and x1>0:
                        point_slope=m*(-x1)-y1
                    elif m>0 and y1<0 and x1<0:
                        point_slope=m*x1-y1
                    elif m<0 and y1>0 and x1>0:
                        point_slope=(-m)*(-x1)+y1
                    elif m<0 and y1>0 and x1<0:
                        point_slope=(-m)*x1+y1
                    elif m<0 and y1<0 and x1>0:
                        point_slope=(-m)*(-x1)-y1
                    elif m<0 and y1<0 and x1<0:
                        point_slope=(-m)*x1-y1
                    print()
                    print(f"Your point slope formula is: y={m}x+{point_slope}")
                else:
                    print("Invalid choice!")
            if  solutions=="2": #2. Quadratic equations
                print("Pick 1 for completing the square \nPick 2 to learn how to factor")
                quadratic=input("Select 1 or 2: ")
                if quadratic=="1": #2.1 completing the square
                    print("Complete the square: (b/2a)^2")
                    print()
                    b=int(input("Enter your 'b'value: "))
                    a=int(input("Enter your 'a' value: "))
                    completing_the_square=(b/(2*a))**2
                    print()
                    print(f"The value after completing the square is: {completing_the_square}")
                elif quadratic=="2": #2.2 learn how to factor
                    print("Factoring is very simple as long as you follow some very simple steps! \n\n1. Identify your your a,b, and c values from ax^2+bx+c"
                          "\n2. Identify if your coefficient is 1 or any other number\n\n")
                    coefficient=input("Is your coefficient 1 or another number? (Enter 1 or another number)")
                    if coefficient=="1": #2.2.1a=1
                        print("\n3. Find 2 numbers that multiply up to your c value and add up your b value (keep in mind negative numbers)"
                              "\n4. rewrite your equation as ax^2+(new number)x+(second new number x)+c \n5. Separate the equation in groups of 2"
                              "and take out the GCF \n6. Set 2 new equations =0 and then find the value of x")
                    elif coefficient=="another number": #2.2.a= another number
                        print("\n3. Multiply a and c together and then find 2 numbers that multiply up to your c value and add up your b value (keep in mind "
                              "negative numbers) \n4. Rewrite your equation as ax^2+(new number)x+(second new number x)+c \n5. Separate the equation in groups of"
                              " 2 and take out the GCF \n6. Set 2 new equations =0 and then find the value of x")
                    else:
                        print("Invalid choice!")
            if solutions=="3":#3. exponential functions
                print("Pick 1 for Parent function \nPick 2 for Exponential growth \nPick 3 for Exponential Decay")
                exponent=input("Select 1,2, or 3: ")
                if exponent=="1": #3.1 parent function
                    print("Parent function: f(x)=ab^x")
                    print()
                    a=int(input("Enter your 'a' value: "))
                    b=int(input("Enter your 'b' value: "))
                    x=int(input("Enter your 'x' value: "))
                    parent_function=a*b**2
                    print()
                    print(f"The result of your parent function is: f(x)={parent_function}")
                elif exponent=="2": #3.2 Exponential growth
                    print("Exponential growth: f(x)= a(1+r)^x")
                    print()
                    a=float(input("Enter your 'a' value: "))
                    r=float(input("Enter your 'r' value in (decimal form): "))
                    x=float(input("Enter your 'x' value: "))
                    exponential_growth=a*(1+r)**x
                    print()
                    print(f"The exponential growth is: {exponential_growth}")
                elif exponent=="3": #3.3 Exponential decay
                    print("Exponential decay: f(x)= a(1-r)^x")
                    print()
                    a=float(input("Enter your 'a' value: "))
                    r=float(input("Enter your 'r' value (in decimal form): "))
                    x=float(input("Enter your 'x' value: "))
                    exponential_decay=a*(1-r)**x
                    print()
                    print(f"The exponential decay is: {exponential_decay}")
                else:
                    print("Invalid choice!")
            if solutions=="4": #4. Quadratic formula
                print(f"Quadratic Formula: x= -b {plus_minus_symbol}(√b^2-4ac)/2a")
                print()
                a=float(input("Enter your 'a' value: "))
                b=float(input("Enter your 'b' value: "))
                c=float(input("Enter your 'c' value: "))
                inside_square_root=b**2-(4*a*c)
                square_root=inside_square_root**0.5
                division=2*a
                quadratic_formula_positive=(-b+square_root)/division
                quadratic_formula_negative=(-b-square_root)/division
                print()
                print(f"The 2 solutions in the quadratic formula are: {quadratic_formula_positive} and {quadratic_formula_negative}")
            if solutions=="5": #5. Simple Interest
                print("Simple interest formula: A=P(1+rt), where P= principal, r= rate, and t= time")
                print()
                p=float(input("Enter your 'Principal' value: "))
                r=float(input("Enter your 'r' value (in decimal form): "))
                t=float(input("Enter your 't' value: "))
                simple_interest=p*(1+r*t)
                print()
                print(f"The simple interest is: {simple_interest}")
            if solutions=="6": #6. compound interest
                print("Compound Interest Formula: A=P(1+r/n)^nt, where P= principal, r= rate, n= number of times compounded, and t= time")
                p=float(input("Enter your 'Principal' value: "))
                r=float(input("Enter your 'r' value (in decimal form): "))
                t=float(input("Enter your 't' value: "))
                n=float(input("Enter your 'n' value: "))
                exponent=n*t
                r_and_n=r/n
                compound_interest=p*(1+r_and_n)**exponent
                print()
                print(f"The compound interest is: {compound_interest}")
            else:
                print("Invalid choice!")

                    
    elif choice=="2": #Geometry
        print("\nWelcome to Geometry! \nPick 1 for formulas \nPick 2 for solutions\n")
        option=input("Select 1 or 2: ")
        if option=="1": #Formulas
            print("\nPick 1 for Distance Formula \nPick 2 for Midpoint Formula \nPick 3 for Slope Formula \nPick 4 for Area and Surface Area of shapes "
                  "\nPick 5 for Circumference and Volume of shapes \nPick 6 for Trigonometric Ratios")
            print()
            formulas=input("Select 1,2,3,4,5 or 6: ")
            if formulas=="1": #1. Distance Formula
                print("The Distance Formula: d=√(x2-x1)^2+(y2-y1)^2")
            elif formulas=="2": #2. Midpoint Formula
                print("The Midpoint Formula: (Xm,Ym)=((x1+x2)/2, (y1+y2)/2)")
            elif formulas=="3": #3. Slope Formula
                print("The slope formula: m=(y2-y1)/(x2-x1)")
            elif formulas=="4": #4. Area and Surface Area of shapes
                print("KEY: \nA=area \nSA=surface area \nP=perimeter \na=apothem \nh=height \nr=radius \nhs=slant height \nl=slant height \nb=base \nB=area of base")
                print()
                print("The Area of a Parallelogram: A=bh \nThe Area of a Trapezoid: A=½h(b1+b2) \nThe Area of a Circle: A=πr^2 "
                      "\nThe Area of Regular Polygon: A=½Pa \nThe surface area of Prism/Cylinder: SA=2B+Ph \nThe surface area of cone: SA=B+πrhs or SA=B+πrl "
                      "\nThe surface area of Regular Pyramid: SA=B+½Phs or SA=B+½Pl \nThe surface area of Sphere: SA=4πr^2")
            elif formulas=="5": #5. Circumference and Volume of shapes
                print("KEY: \nC=circumference \nV=volume \nr=radius \nd=diameter \nB=area of base \nh=height")
                print()
                print("The circumference of Circle: C=2πr or C=πd \nVolume of Prism/Cylinder: V=Bh \nVolume of Cone: 0.333Bh \n Volume of Regular Pyramid: "
                      "V=0.333Bh \nVolume of sphere: V=1.333πr^3")
            elif formulas=="6": #6. Trigonometric Ratios
                print("Trigonometric formula for Sine: SinΘ= Opposite/Hypotenuse \nTrigonometric formula for Cosine: CosΘ= Adjacent/Hypotenuse "
                      "\nTrigonometric formula for Tangent: TanΘ= Opposite/Adjacent")
            else:
                print("Invalid choice!")
                
        elif option=="2": #solutions
            print("\nPick 1 for Distance Formula \nPick 2 for Midpoint Formula \nPick 3 for Slope Formula \nPick 4 for Area and Surface Area of shapes "
                  "\nPick 5 for Circumference and Volume of shapes")
            solutions=input("Select 1,2,3,4 or 5: ")
            if solutions=="1": #1. Distance Formula
                print("Distance Formula: d=√(x2-x1)^2+(y2-y1)^2")
                print()
                x1=float(input("Enter your 'x1' value: "))
                y1=float(input("Enter your 'y1' value: "))
                x2=float(input("Enter your 'x2' value: "))
                y2=float(input("Enter your 'y2' value: "))
                x_value=(x2-x1)**2
                y_value=(y2-y1)**2
                inside_square_root=x_value+y_value
                square_root=inside_square_root**0.5
                print()
                print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {square_root}.")
            elif solutions=="2": #2. Midpoint Formula
                print("Midpoint formula: (Xm,Ym)=((x1+x2)/2, (y1+y2)/2)")
                print()
                x1=float(input("Enter your 'x1' value: "))
                y1=float(input("Enter your 'y1' value: "))
                x2=float(input("Enter your 'x2' value: "))
                y2=float(input("Enter your 'y2' value: "))
                x_value=(x1+x2)/2
                y_value=(y1+y2)/2
                print()
                print(f"The midpoint between ({x1},{y1}) and ({x2},{y2}) is ({x_value},{y_value})")
            elif solutions=="3": #3. slope formula
                print("Slope formula: m=(y2-y1)/)x2-x1)")
                print()
                y1=int(input("Enter your 'Y1' value: "))
                y2=int(input("Enter your 'Y2' value: "))
                x1=int(input("Enter your 'X1' value: "))
                x2=int(input("Enter your 'X2' value: "))
                slope=(y2-y1)/(x2-x1)
                print()
                print(f'Your slope is: m= {slope}')
            elif solutions=="4": #4. Area and Surface Area of shapes
                print("KEY: \nA=area \nSA=surface area \nP=perimeter \na=apothem \nh=height \nr=radius \nhs=slant height \nl=slant height \nb=base \nB=area of base")
                print()
                print("Pick 1 for Area of a Parallelogram \nPick 2 for Area of a Trapezoid \nPick 3 for Area of a Circle \nPick 4 for Area of a Regular"
                               " Polygon \nPick 5 for Surface Area of a Prism/Cylinder \nPick 6 for Surface Area of a Cone \nPick 7 for Surface Area of a"
                               " Regular Pyramid \n Pick 8 for Surface Area of a Sphere")
                areas=input("Select 1,2,3,4,5,6,7, or 8: ")
                if areas=="1": #4.1 Area of a Parallelogram
                    print("Area of a Parallelogram: A=bh")
                    print()
                    b=float(input("Enter your 'b' value: "))
                    h=float(input("Enter your 'h' value: "))
                    parallelogram=b*h
                    print()
                    print(f"The area of the parallelogram is: {parallelogram}")
                elif areas=="2": #4.2 Area of a Trapezoid
                    print("Area of a Trapezoid: A=½h(b1+b2)")
                    print()
                    h=float(input("Enter your 'h' value: "))
                    b1=float(input("Enter your 'b1' value: "))
                    b2=float(input("Enter your 'b2' value: "))
                    trapezoid=0.5*h*(b1+b2)
                    print()
                    print(f"The area of the trapezoid is: {trapezoid}")
                elif areas=="3": #4.3 Area of a circle
                    print("Area of a circle: A=πr^2")
                    print()
                    r=float(input("Enter your 'r' value: "))
                    circle=3.14*(r**2)
                    print()
                    print(f"The area of the circle is: {circle}")
                elif areas=="4": #4.4 Area of regular polygon
                    print("Area of a Regular Polygon: A=½Pa")
                    print()
                    p=float(input("Enter your 'P' value: "))
                    a=float(input("Enter your 'a' value: "))
                    polygon=0.5*p*a
                    print()
                    print(f"The area of the regular polygon is: {polygon}")
                elif areas=="5": #4.5 Area of a prism/cylinder
                    print("Surface Area of a prism/cylinder: SA=2B+Ph")
                    print()
                    b=float(input("Enter your 'B' value: "))
                    p=float(input("Enter your 'P' value: "))
                    h=float(input("Enter your 'h' value: "))
                    prism=(2*b)+(p*h)
                    print()
                    print(f"The surface area of the prism/cylinder: {prism}")
                elif areas=="6": #4.6 Surface Area of a cone
                    print("Surface Area of a cone: SA=B+πrhs or SA=B+πrl (NOTE: hs and l represent the same thing)")
                    print()
                    b=float(input("Enter your 'B' value: "))
                    r=float(input("Enter your 'r' value: "))
                    hs_or_l=float(input("Enter your 'hs' or 'l' value: "))
                    cone=(3.14*r*hs_or_l)+b
                    print()
                    print(f"The surface area of the cone is: {cone}")
                elif areas=="7": #4.7 Surface Area of a Regular Pyramid
                    print("Surface Area of a Regular Pyramid: SA=B+½Phs or SA=B+½Pl (NOTE: hs and l represent the same thing)")
                    print()
                    b=float(input("Enter your 'B' value: "))
                    p=float(input("Enter your 'P' value: "))
                    hs_or_l=float(input("Enter your 'hs' or 'l' value: "))
                    pyramid=(0.5*p*hs_or_l)+b
                    print()
                    print(f"The surface area of the regular pyramid is: {pyramid}")
                elif areas=="8": #4.8 Surface Area of a sphere
                    print("Surface Area of a sphere: SA=4πr^2")
                    print()
                    r=float(input("Enter your 'r' value: "))
                    sphere=(r**2)*3.14*4
                    print()
                    print(f"The surface area of the sphere is: {sphere:}")
                else:
                    print("Invalid choice!")
            elif solutions=="5": #5. Circumference and Volume of shapes
                print("KEY: \nC=ciCircumference \nV=volume \nr=radius \nd=diameter \nB=area of base \nh=height")
                print()
                print("Pick 1 for Circumference of a circle \nPick 2 for Volume of a prism/cylinder \nPick 3 for Volume of a cone \nPick 4 for Volume of a "
                      "regular pyramid \nPick 5 for Volume of a sphere")
                volume=input("Select 1,2,3,4, or 5: ")
                if volume=="1": #5.1 Circumference of a circle
                    print("Circumference of a circle: C=2πr or C=πd")
                    print()
                    print("Pick 1 for solving circumference with radius \nPick 2 for solving circumference with diameter")
                    r_and_d=input("Select 1 or 2: ")
                    if r_and_d=="1": #Circumference with radius
                        r=float(input("Enter your 'r' value: "))
                        circumference=r*3.14*2
                        print()
                        print(f"The Circumference of the circle is: {circumference}")
                    elif r_and_d=="2": #Circumference with diameter
                        d=float(input("Enter your 'd' value: "))
                        circumference=3.14*d
                        print()
                        print(f"The Circumference of the circle is: {circumference}")
                    else:
                        print("Invalid choice!")
                elif volume=="2": #5.2 volume of a prism/cylinder
                    print("Volume of a prism/cylinder: V=Bh")
                    print()
                    b=float(input("Enter your 'B' value: "))
                    h=float(input("Enter your 'h' value: "))
                    prism=b*h
                    print()
                    print(f"The volume of the prism/cylinder is: {prism}")
                elif volume=="3": #5.3 Volume of a cone
                    print(f"Volume of a cone: V=0.333Bh")
                    print()
                    b=float(input("Enter your 'B' value: "))
                    h=float(input("Enter your 'h' value: "))
                    cone=0.333*b*h
                    print()
                    print(f"The volume of the cone is: {cone}")
                elif volume=="4": #5.4 Volume of regular pyramid
                    print("Volume of a regular pyramid: V=0.333Bh")
                    print()
                    b=float(input("Enter your 'B' value: "))
                    h=float(input("Enter your 'h' value: "))
                    print()
                    regular_pyramid=0.333*b*h
                    print(f"The volume of the regular pyramid is: {regular_pyramid}")
                elif volume=="5": #5.5 Volume of a sphere
                    print("Volume of a Sphere: V=1.333πr^3")
                    r=float(input("Enter your 'r' value: "))
                    sphere=(r**3)*1.333*3.14
                    print(f"The volume of the sphere is {sphere}")
                else:
                    print("Invalid choice")
            else:
                print("Invalid choice")

                
    elif choice=="3":
        print("\nWelcome to Pre-Calculus! Here we will provide all formulas you will need during your Pre-Calculus semester!")
        print("\nPick 1 for Exponential and Logarithmic Functions \nPick 2 for Trigonometry \nPick 3 for Solving equations with Trigonometry")
        print()
        calc=input("Select 1,2, or 3: ")
        if calc=="1":
            print("\nPick 1 for Transformations and logarithmic Function \nPick 2 for Logarithmic Functions \nPick 3 for Properties of Algorithms \nPick 4"
                  " for Exponential and Logarithmic equations \nPick 5 for Exponential Growth and Decay Modeling Data\n")
            logs=input("Select 1,2,3,4 or 5: ")
            if logs=="1":
                print("\nTransformations: \n - g(x)=b^x +c Shifts f(x) upward c units \n - g(x)=b^x -c Shifts f(x) downward c units \n"
                  " - g(x)=b^x+c Shifts f(x) left c units \n - g(x)=b^x-c Shifts f(x) right C units \n - g(x)=-b^x Reflects f(x) about the x-axis \n"
                  " - g(x)=b^-x Reflects f(x) about the y-axis \n - g(x)=cb^x Vertically stretches the graph of f(x) if c>1 and shrinks if 0<c<1 \n"
                  " - g(x)=b^cx Horizontally stretches the graph of f(x) if c>1 and stretches if 0<c<1")
                print("\nCompound Interest: \n Compounding periods per year: A=P(1+r/n)^nt \n Continuous compounding:A=Pe^rt")
            elif logs=="2":
                print("\nProperties of Common Logarithms: \n General properties: \n  - logb1=0 \n  - logbb=1 \n  - logbb^x=x \n  - b^logbx=x \n "
                      "Common Logarithms: \n  - log1=0 \n  - log10=1 \n  - log10^x=x \n  - 10^logx=x")
                print("\nProperties of Natural Logarithms: \n General properties: \n  - logb1=0 \n  - logbb=1 \n  - logbb^x=x \n  - b^logbx=x \n Common"
                      "Logarithms: \n  - ln1=0 \n  - lne=1 \n  - lne^x=x \n  - e^lnx+x")
            elif logs=="3":
                print("\nExpanding logarithms: \n - The Product rule: logb(MN)=logbM + logbN \n - The Quotient rule: logb(M/N)=logbM-logbN \n - The Power rule: "
                      "logbM^p=plogbM \nCondensing logarithms: \n - The Product rule: logbM + logbN=logb(MN) \n - The Quotient rule: logbM-logbN=logb(M/N) \n - The"
                      "Power Rule: plogbM=logbM^p \nThe Change-of-base Property: \n  - logbM=logaM/logab \n Common logarithms: \n  - logbM=logM/logb \n Natural"
                      " logarithms \n  - logbM=lnM/lnb")
            elif logs=="4":
                print("\nExponential Equations, each side is equal power of same base: \n - b^m=b^n, then M=N \nUse logs to solve exponential equations: \n - "
                      "b^x=xlnb or lne^x=x or log10^x=x \nUse definition of logs to solve logarithmic Equations: \n - logbM=c means b^c=M")
            elif logs=="5":
                print("\nExponential growth and Decay Models: \n f(t)=A0e^kt \n  - A0=original amount \n  - t=time \n  - k=constant \nLogistic Growth model: "
                      "\n f(t)=c/1+ae^-bt \n  - a,b,c are constants \n  - a>0 and b>0 \nNewton's law of Cooling: \n T=C+(T0-C)e^kt \n  - C=Constant Temperature"
                      "\n  - T0=Initial Temperature \n  - k=Negative Constant")
            else:
                print("Invalid option!")
        elif calc=="2":
            print("Pick 1 for Angles and Radian Measure \nPick2 for the Unit Circle \nPick 3 for Right Triangle Trigonometry \nPick 4 for Trigonometric Functions"
                  "of Any angle")
            print()
            trig=input("Select 1,2,3 or 4: ")
            if trig=="1":
                print("\nRadian Measure: \n Θ=s/r \n  - s=arc length \n  - r=radius \n  - Θ=central angle \nDegrees to Radians: \n degrees x π/180 \nRadians to"
                        "Degrees: \n radians x 180/π \nCoterminal angles: \n Θ" +plus_minus_symbol+ "2kπ or Θ" +plus_minus_symbol+ "360k \nArc Lenght: \n"
                      " s=Θr \n  - s=arc length \n  - r=radius \n  - Θ=central angle \nLinear and Angular Speed: \n Linear: v=s/t \n Angular: w=Θ/t \nLinear"
                      " Speed in terms of Angular Speed: \n v=rw")
            elif trig=="2":
                print("\nTrig Functions: \n - Sin(x)=1/Csc(x) \n - Cos(x)=1/Sec(x) \n - Tan(x)=Sin(x)/Cos(x) \n - Csc(x)=1/Sin(x) \n - Sec(x)=1/Cos(x)"
                      "\n - Cot(x)=Cos(x)/Sin(x)\n\nUnit Circle (Degrees,radians,(cos(x),sin(x)), tan(x)):"
                      "\n 0°, 0, (1,0), 0"
                      "\n 30°, π/6, (√3/2,1/2), √3/3"
                      "\n 45°, π/4, (√2/2,√2/2), 1"
                      "\n 60°, π/3, (1/2,√3/2), √3"
                      "\n 90°, π/2, (0,1), undef"
                      "\n 120°, 2π/3, (-1/2,√3/2), -√3"
                      "\n 135°, 3π/4, (-√2/2,√2/2), -1"
                      "\n 150°, 5π/6, (-√3/2,1/2), -√3/3"
                      "\n 180°, π, (-1,0), 0"
                      "\n 210°, 7π/6, (-√3/2,-1/2), √3/3"
                      "\n 225°, 5π/4, (-√2/2,-√2/2), 1"
                      "\n 240°, 4π/3, (-1/2,-√3/2), √3"
                      "\n 270°, 3π/2, (0,-1), undef"
                      "\n 300°, 5π/3, (1/2,-√3/2), -√3"
                      "\n 315°, 7π/4, (√2/2,-√2/2), -1"
                      "\n 330°, 11π/6, (√3/2,-1/2), -√3/3"
                      "\n 360°, 2π, (1,0), 0"
                      "\n\nEven and Odd Trig functions: \n Even: \n  - Cos(x) \n  - Sec(x) \n Odd: \n  - Sin(x) \n  - Csc(x)  \n  - Tan(x) \n  - Cot(x)"
                      "\n\nPeriod Function: \n f(t+p)=f(t) \nFundamental Identities: \n Reciprocal identities: \n  - Sin(x)=1/Csc(x) \n  - Cos(x)=1/Sec(x) \n  - "
                      "Tan(x)=1/Co(x)t \n  - Csc=1/Sin(x) \n  - Sec(x)=1/Cos(x) \n  - Cot(x)=1/Tan(x) \n Quotient Identities: \n  - Tan(x)=Sin(x)/Cos(x)"
                      "\n  - Cot(x)=Cos(x)/Sin(x) \n Pythagorean Identities: \n  - Cos^2 x + Sin^2 x = 1")
            elif trig=="3":
                print("\n0°, 0, (1,0), 0 \n30°, π/6, (√3/2,1/2), √3/3 \n45°, π/4, (√2/2,√2/2), 1 \n60°, π/3, (1/2,√3/2), √3")
            elif trig=="4":
                print("\nDistance formula: d=√(x2-x1)^2+(y2-y1)^2 \n\nSigns of Trigonometric Function: \n  You can remember with All Students Take Calculus"
                      "\n  - A=All are positive on 1st quadrant \n  - S=Only Sin(x) is positive on the 2nd quadrant \n  - T=Only Tan(x) is positive on the 3rd"
                      "quadrant \n  - C=Only Cos(x) is positive on the 4th quadrant")
                reference_angles=['2nd quadrant: 180-Θ or π-Θ','3rd quadrant: 180+Θ or π+Θ','4th quadrant:360-Θ or 2π-Θ']
                quadrant=input("Choose 1 for 2nd quadrant \nChoose 2 for 3rd quadrant \nChoose 3 for 4th quadrant \nChoose 4 for all quadrants \n")
                if quadrant=="1":
                    print(reference_angles[0])
                elif quadrant=="2":
                    print(reference_angles[1])
                elif quadrant=="3":
                    print(reference_angles[2])
                elif quadrant=="4":
                    print(reference_angles)
                else:
                    print("Invalid option!")
                answer=input("Do you need another reference angle? (yes or no) ")
                while answer=="yes":
                    if answer=="yes":
                        quadrant=input("Choose 1 for 2nd quadrant \nChoose 2 for 3rd quadrant \nChoose 3 for 4th quadrant \nChoose 4 for all quadrants \n")
                        if quadrant=="1":
                            print(reference_angles[0])
                        elif quadrant=="2":
                            print(reference_angles[1])
                        elif quadrant=="3":
                            print(reference_angles[2])
                        elif quadrant=="4":
                            print(reference_angles)
                        else:
                            print("Invalid option!")
                    else:
                        print("Ok, moving on to graphing!")
                    answer=input("Do you need another reference angle? (yes or no): ")
                print("\nGraphs of y=Asin(Bx-C) and y=Acos(Bx-C): \n - Amplitude=|A|-1/2 (This is the height of the graph) \n - Period=2π/B (How long before the"
                      " pattern repeats \n - Phase Shift=C/B (The location where the first period starts")
                print("\nInverse Trigonometric Functions: ")
                inverse_sin_func=("y=sin^-1 x")
                reciprocal_sin_func=("y=(sinx)^-1 =1/sinx=cscx")
                inverse_cos_func=("y=cos^-1 x")
                reciprocal_cos_func=("y=(cosx)^-1 =1/cosx=secx")
                inverse_tan_func=("y=tan^-1 x")
                reciprocal_tan_func=("y=(tanx)^-1 =1/tanx=cotx")
                sin_functions=inverse_sin_func+"\n"+reciprocal_sin_func
                cos_functions=inverse_cos_func+"\n"+reciprocal_cos_func
                tan_functions=inverse_tan_func+"\n"+reciprocal_tan_func
                trig=input("Choose 1 for Inverse of Sin Functions \nChoose 2 for Inverse of Cos functions \nChoose 3 for Inverse of Tan functions \n")
                if trig=="1":
                    print(sin_functions)
                elif trig=="2":
                    print(cos_functions)
                elif trig=="3":
                    print(tan_functions)
                else:
                    print("Invalid choice!")
                answer=input("\nDo you need another Inverse Trigonometric Functions? (yes or no) ")
                while answer=="yes":
                    if answer=="yes":
                        trig=input("Choose 1 for Inverse of Sin Functions \nChoose 2 for Inverse of Cos functions \nChoose 3 for Inverse of Tan functions \n")
                        if trig=="1":
                            print(sin_functions)
                        elif trig=="2":
                            print(cos_functions)
                        elif trig=="3":
                            print(tan_functions)
                        else:
                            print("Invalid choice!")
                    else:
                        print("We have reached the end of this chapter, make a new selection!")
                    answer=input("\nDo you need another Inverse Trigonometric Functions? (yes or no) ")
        elif calc=="3":
            print("Pick 1 for Sum and Difference Formulas \nPick2 for Double Angle, Power-Reducing, and Half Angle formulas \nPick 3 for Product to Sum and Sum to"
                  " Product formulas \nPick 4 for Trigonometric equations \nPick 5 for the Law of Sines formulas \nPick 6 for the Law of Cosines formulas \nPick 7"
                  " for Polar and Rectangular coordinates formulas \nPick 8 for Complex numbers formulas\n")
            formulas=input("Select 1,2,3,4,5,6,7 or 8: ")
            if formulas=="1":
                print("- Cos(α+ß)=cosα•cosß-sinα•sinß\n- Cos(α-ß)=cosα•cosß+sinα•sinß\n- Sin(α+ß)=sinα•cosß+cosα•sinß\n- Sin(α-ß)=sinα•cosß-cosα•sinß\n"
                      "- Tan(α+ß)=(tanα+tanß)/1-tanαtanß\n- Tan(α-ß)=(tanα-tanß)/1+tanαtanß\n")
            elif formulas=="2":
                angles=['- Sin2Θ=2sinΘcosΘ\n- Cos2Θ=cos^2 Θ-sin^2 Θ\n- Tan2Θ=2tanΘ/1-tan^2 Θ','- Sin^2 Θ=1-cos2Θ/2\n- cos^2 Θ=1+cos2Θ/2\n'
                        '- tan^2 Θ=1-cos2Θ/1+cos2Θ','- sinα/2='+plus_minus_symbol+'√1-cosα/2\n- cosα/2='+plus_minus_symbol+'√1+cosα/2\n- '
                        'tanα/2='+plus_minus_symbol+'√1-cosα/1+cosα']
                angle=input("Select 1 for Double Angles \nSelect 2 for Power reducing formulas \nSelect 3 for Half Angles \nSelect 4 for all of the above \n")
                if angle=="1":
                    print(angles[0])
                elif angle=="2":
                    print(angles[1])
                elif angle=="3":
                    print(angles[2])
                elif angle=="4":
                    print(angles)
                else:
                    print("Invalid choice!")
                answer=input("\nDo you need another type of formulas for angles? (yes or no) ")
                while answer=="yes":
                    if answer=="yes":
                        angle=input("Select 1 for Double Angles \nSelect 2 for Power reducing formulas \nSelect 3 for Half Angles \nSelect 4 for all"
                                          "of the above \n")
                        if angle=="1":
                            print(angles[0])
                        elif angle=="2":
                            print(angles[1])
                        elif angle=="3":
                            print(angles[2])
                        elif angle=="4":
                            print(angles)
                        else:
                            print("Invalid choice!")
                    else:
                        print("Ok! Moving on to product to sum and sum to product formulas")
                    answer=input("\nDo you need another type of formulas for angles? (yes or no) ")
            elif formulas=="3":
                product_to_sum=('sinα•sinß=½[cos(α-ß)-cos(α+ß]) \n','cosαcosß=½[cos(α-ß)+cos(α+ß] \n','sinαCosß=½[sin(α+ß)+sin(α-ß) \n','sinαCosß=½[sin(α+ß)-sin(α-ß)')
                sum_to_product=('sinα+ß=2sinα+ß/2•cosα-ß/2 \n','sinα-sinß=2sinα-ß/2•cosα+ß/2 \n','cosα+cosß=2cosα+ß/2•cosα-ß/2 \n','cosα-cosß=-2sinα+ß/2•cosα-ß/2')
                both=product_to_sum+sum_to_product
                choice=input("Select 1 for Product to Sum \nSelect 2 for Sum to Product \nSelect 3 for Both \n")
                if choice=="1":
                    print(product_to_sum)
                elif choice=="2":
                    print(sum_to_product)
                elif choice=="3":
                    print(both)
                else:
                    print("Invalid choice!")
                answer=input("\nDo you need another type of formulas for angles? (yes or no) ")
                while answer=="yes":
                    if answer=="yes":
                        choice=input("Select 1 for Product to Sum \nSelect 2 for Sum to Product \nSelect 3 for Both \n")
                        if choice=="1":
                            print(product_to_sum)
                        elif choice=="2":
                            print(sum_to_product)
                        elif choice=="3":
                            print(both)
                        else:
                            print("Invalid choice!")
                    else:
                        print("Ok! Moving on to Trigonometric equations!")
                    answer=input("\nDo you need another type of formulas for angles? (yes or no) ")
            elif formulas=="4":
                print("Trigonometric Equations: \n General solution: \n  - x=Θ+2nπ {sin and Cos) \n  - x=Θ+nπ {tan} \n Particular Solution: \n  - [0,2π)")
            elif formulas=="5":
                print("\nThe Law of Sines: \n - a/sinA = b/sinB = c/sinC \nArea of an Oblique Triangle: \n - Area=½bcSinA=½abSinC = ½acSinB")
            elif formulas=="6":
                print("\nThe Law of Cosines: \n - a^2=b^2+c^2-2bcCosA \n - b^2=a^2+c^2-2acCosB \n - c^2=a^2+b^2-2abCosC"
                      "\nHeron's Formula for the area of a triangle: \n - Area=√s(s-a)(s-b)(s-c) \n  - s=½(a+b+c)")
            elif formulas=="7":
                print("Pick 1 for Polar to Rectangular \nPick 2 for Rectangular to Polar \nPick 3 for both \n")
                coordinates=input("Select 1,2, or 3: ")
                if coordinates=="1":
                    print("\nPolar Coordinates to Rectangular Coordinates: \n - (r,Θ) -> (x,y) \n  - x=rCosΘ \n  - y=rSinΘ")
                elif coordinates=="2":
                    print("\nRectangular Coordinates to Polar Coordinates: \n - (x,y) -> (r,Θ) \n  - r^2 = x^2 + y^2 \n  - Θ=tan^-1 (y/x)")
                elif coordinates=="3":
                    print("\nPolar Coordinates to Rectangular Coordinates: \n - (r,Θ) -> (x,y) \n  - x=rCosΘ \n  - y=rSinΘ \n\nRectangular Coordinates to Polar"
                          "Coordinates: \n - (x,y) -> (r,Θ) \n  - r^2 = x^2 + y^2 \n  - Θtan^-1 (y/x)")
                else:
                    print("Invalid choice!")
                answer=input("\nDo you need another type of formulas for angles? (yes or no) ")
                while answer=="yes":
                    if answer=="yes":
                        print("Pick 1 for Polar to Rectangular \nPick 2 for Rectangular to Polar \nPick 3 for both \n")
                        coordinates=input("Select 1,2, or 3: ")
                        if coordinates=="1":
                            print("\nPolar Coordinates to Rectangular Coordinates: \n - (r,Θ) -> (x,y) \n  - x=rCosΘ \n  - y=rSinΘ")
                        elif coordinates=="2":
                            print("\nRectangular Coordinates to Polar Coordinates: \n - (x,y) -> (r,Θ) \n  - r^2 = x^2 + y^2 \n  - Θtan^-1 (y/x)")
                        elif coordinates=="3":
                            print("\nPolar Coordinates to Rectangular Coordinates: \n - (r,Θ) -> (x,y) \n  - x=rCosΘ \n  - y=rSinΘ \n\nRectangular Coordinates"
                                  "to Polar Coordinates: \n - (x,y) -> (r,Θ) \n  - r^2 = x^2 + y^2 \n  - Θtan^-1 (y/x)")
                        else:
                            print("Invalid Choice!")
                    else:
                        print("Ok! This is the end of the section, please make a new selection")
                    answer=input("\nDo you need another type of formulas for angles? (yes or no) ")
            elif formulas=="8":
                print("\nComplex numbers: \n The absolute value of a complex Number: \n  |z|=|a+bi|=√a^2 + b^2 \n\n Polar form of a complex number: "
                      "\n  z=r(cosΘ+isinΘ) \n\n Product of two complex numbers in polar form: \n  Z1Z2=r1r2[cos(Θ1+Θ2)+isin(Θ1+Θ2)]"
                      "\n\n Quotient of two complex numbers in Polar form: \n  Z1/Z2=r1/r2[cos(Θ1-Θ2)+isin(Θ1-Θ2)] \n\n DeMoivre's Theorem: \n  "
                      "Z^n=[r(cosΘ+isinΘ)]^n = r^n (cosnΘ+isinΘ) \n\n DeMoivre's Theorem for finding Complex Roots: Zk=n√r [cos(Θ+2πk/n)+isin(Θ+2πk/n)"
                      "\n   *For Degrees switch '2π' with '360'*") 

