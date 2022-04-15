class foo:
    class_name_space_var = "클래스 맴버"                 # 클래스 멤버

    def set_instance_name_space_var(self, x):
        self.instance_name_space_var = x         # 인스턴스 멤버
    def get_nstance_name_space_var(self):
        return self.instance_name_space_var

def test_member():
    p = foo()
    p.set_instance_name_space_var("인스턴스 맴버")
    
    # Instance name space에 class_name_space_var가 없으므로
    # class name space에서 class_name_space_var 변수를 찾는다.
    # ( 자바스크립트의 prototype chaining과 비슷 )
    print('{0}, {1}'.format(p.instance_name_space_var, p.class_name_space_var))

test_member()