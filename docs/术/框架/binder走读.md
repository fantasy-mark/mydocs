http://aospxref.com/android-10.0.0_r47/

```java
// 调用关系链
// /frameworks/native/cmds/servicemanager/service_manager.c
	main
		bs = binder_open(driver, 128*1024);
		if (binder_become_context_manager(bs)) {
		binder_loop(bs, svcmgr_handler);
// /frameworks/native/cmds/servicemanager/binder.c
		bs->fd = open(driver, O_RDWR | O_CLOEXEC);
		int result = ioctl(bs->fd, BINDER_SET_CONTEXT_MGR_EXT, &obj);
		result = ioctl(bs->fd, BINDER_SET_CONTEXT_MGR, 0);
		res = ioctl(bs->fd, BINDER_WRITE_READ, &bwr);
// 驱动层的binder...
```



![binder与各系统服务](binder2fwk.drawio)



* 为什么使用socket作为zygote通信

1. zygote进程进程无法保证注册Binder时，init进程已经完成SeverManger的初始化
2. Binder服务端会创建线程来接收Binder驱动数据，而fork多线程的进程容易造成死锁
3. 如果zygote进程使用Binder作为通信，则每次fork出来的进程多使用Binder对象消耗的内存