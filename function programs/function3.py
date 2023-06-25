'''The below picture includes five geometrical shapes. You have to write Python code that includes five different functions: sphere(), cylinder(), cone(), rectangular_prism(), and triangular_prism(). You should get the respective values in the formula for the shapes, and they should be passed to the function as a parameter. If any of the shapes include "π” (pi), then pi value should be passed as the default argument, and functions should return the SURFACE AREA AND VOLUME of the respective geometrical shapes. 
The formula for calculating the surface area and volume of the shapes is given in the picture.'''
def geo_shapes(r,h,w,b,l,s,pi=3.14):
    sa_sphere=4*pi*r*r
    v_sphere=4/3*pi*r*r*r
    sa_cylinder=2*pi*r*r+2*pi*r*h
    v_cylinder=pi*r*r*h
    sa_cone=pi*r*s+pi*r*r
    v_cone=1/3*pi*r*r*h
    sa_rp=2*(l*w+l*h+w*h)
    v_rp=l*w*h
    sa_tp=b*h+2*l*s+l*b
    v_tp=1/2*(b*l)*h
    return(sa_sphere,v_sphere,sa_cylinder,v_cylinder,sa_cone,v_cone,sa_rp,v_rp,sa_tp,v_tp)
sa_sphere,v_sphere,sa_cylinder,v_cylinder,sa_cone,v_cone,sa_rp,v_rp,sa_tp,v_tp=geo_shapes(r=3,h=10,w=2,b=2,l=12,s=6,pi=3.14)
print("the surface area and volume of sphere:",sa_sphere,v_sphere)
print("the surface area and volume of cylinder:",sa_cylinder,v_cylinder)
print("the surface area and volume of cone:",sa_cone,v_cone)
print("the surface area and volume of rectangular prism:",sa_rp,v_rp)
print("the surface area and volume of triangular prism:",sa_tp,v_tp)
