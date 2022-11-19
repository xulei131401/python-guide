# __new__是在实例创建之前被调用的，用于创建实例然后返回该实例对象，是个静态方法。__new__必须要有返回值，也就是返回实例化出来的实例。
# __new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
# __new__至少要有一个参数cls，代表当前类
# __init__是实例对象创建完成后被调用，然后设置对象属性的一些初始值，通常用在初始化一个类实例的时候，是一个实例方法。
# __init__的参数self就是__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值（__init__() should return None）。
