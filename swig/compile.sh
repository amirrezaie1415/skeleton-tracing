swig -python trace_skeleton.i
gcc -O3 -fPIC -c trace_skeleton.c trace_skeleton_wrap.c -I/home/swissinspect/miniconda3/envs/paal/include/python3.9
gcc -shared *.o -o _trace_skeleton.so -L/home/swissinspect/miniconda3/envs/paal/lib -lpython3.9

# quick tests
# python3 -i -c "import trace_skeleton; trace_skeleton.trace('\0\0\0\1\1\1\0\0\0',3,3); print(trace_skeleton.len_polyline());"
# python3 -i -c "import trace_skeleton; print(trace_skeleton.from_list([0,0,0,1,1,1,0,0,0],3,3))"
python3 example.py

