# How-To

0) Ocaml env setup  
  a) `opam init --disable-sandboxing`  
  b) `opam sw create 4.12.0`  


1) Install Ocaml JST  
  a) Repo in `/dev/ocaml-jst`  
  b) Repo link: [Github](https://github.com/ocaml-compiler-research/ocaml-jst)  
  c) Install command  
  <code> git clean -dfx && ./tools/autogen && ./configure --prefix=`pwd`/../_install/jst  --disable-ocamldoc --enable-warn-error  --enable-ocamltest && make -j16 world.opt && make install </code>  
  d) Installs into `/dev/_install/jst`  

2) Install Dune  
 a) Repo in `/dev/dune`  
 b) Repo link: [Github](https://github.com/ocaml-flambda/dune.git)  
 c) Install commands  
 <code>git checkout origin/special_dune</code>  
 <code>make release</code>  
 d) Installs into `???`  

3) Install Flambda Backend  
 a) Repo in `/dev/flambda-backend`  
 b) Repo link: [Github](https://github.com/ocaml-flambda/flambda-backend)  
 c) Install command  
 <code>git clean -dfx && autoconf && ./configure --prefix=`pwd`/../_install/fl --enable-middle-end=flambda --with-dune=`pwd`/../dune/dune.exe && make -j16 && make install</code>  
 d) Installs into `/dev/_install/fl`  

4) Install LLVM  
 a) Repo in `/dev/llvm_project`  
 b) Repo link: [Github](https://github.com/llvm/llvm-project)  
 c) Install commands  
 <code>git checkout llvmorg-13.0.0</code>  
 <code>CLANG_TMP_DIR=/cdev/tmp TMPDIR=/cdev/tmp cmake -G Ninja ../llvm-project/llvm/ -DLLVM_TARGETS_TO_BUILD="X86" -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLLVM_ENABLE_ASSERTIONS=On -DLLVM_ENABLE_PROJECTS="clang;clang-tools-extra;libcxx;libcxxabi;libunwind;lldb;compiler-rt;lld" -DCMAKE_INSTALL_PREFIX="/cdev/llvm_install"</code>  
 d) Installs into `/dev/llvm_install`  
 