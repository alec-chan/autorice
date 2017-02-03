echo "creating tarball from ../test_rice/"
tar -cvf test_rice.tar ../test_rice/
echo "installing test_rice with autorice..."
python ../autorice.py --install autorice_tests/test_rice.tar
echo "testing installation of test_rice (if rice installation was successful you will see output below)"
cat ~/test.txt
echo "uninstalling test_rice"
rm -r ~/autorice/rices/test_rice
echo "testing complete."