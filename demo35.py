def demo35(par1, par2, **kwargs):
    print(f"fixed parameter1={par1}, parameter2={par2}")
    for k, v in kwargs.items():
        print(f"flexible key={k}, value={v}")


demo35("Hello", "World")
demo35(par1="Hi", par2="welcome", name="PYKT", duration=35, instructor="Mark Ho")
passObject = {"name": "PYKT", "duration": 35, "instructor": "Mark Ho"}
demo35(par1="try", par2="again", **passObject)