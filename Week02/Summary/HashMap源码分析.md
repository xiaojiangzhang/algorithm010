一、定义

​	HashMap是一种基于hashTable的实现类，基本结构为key-value。key不允许重复，value允许重复。key，value允许为null；

二、HashMap的数据结构：

​		1.8之前：使用数组（已Hash值作为索引）+ 链表（解决Hash冲突）结构进行存储；

​		1.8之后：使用数组+链表（红黑树<链表长度大于8时>）

三、源码分析（1.8）

​	1、HashMap的hash算法

```java
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
```

​		1）key为null时，哈希值为0；key不为null时：

​				① 调用key的的hashcode方法获取一个int类型（32位）的值h;

​				② 将32位的int值h分为高16位（从左向由数16位）和低16位（从右向左数16位），将第一步获取的值h右移16位后，h变成高16位（16个					 0）+ 低16位（在右移之前的高16位）；

​				③ 将初始值h与右移16位后的h进行异或（^）操作（1000 ^ 1011 = 0011，同位相同则为0，同位相异则为1），

​		 2）为什么要将直接调用hashcode方法获取的哈希值与右移16位的值进行异或操作？

​				原值h与h>>>16的值进行异或操作后，实际是将高16位与低16位进行异或操作，这样就将高位也参与运算。例如：

​				                              											高16位	                              低16位

​				          											 h:	0010110111000101           0111010001110011

​			 											k:h>>>16:    0000000000000000           0010110111000101

​                       											h^k:    0010110111000101           0101100110110110

​				若直接使用h作为哈希值，当HashMap的长度为16（2^4），只有低16位的后四位（0011）有效，根据这四位运算出的哈希值范围很小，当				数据比较多时，很容易造成哈希碰撞。而使用异或操作后，使用的后四位实际是高16位的后四位和低16位的后四位进行异或操作后的结果，				这会明显的降低哈希碰撞；

​	2、添加元素（put）操作

​			1）寻址操作

​					示例代码第43行：p = tab[i = (n - 1) & hash]，为什么不直接使用hash值对长度n进行取模（常规做法），而是将长度减1后与哈希值进行与					操作，并且为什么要减1？

​					由于HashMap中规定了哈希表的长度都是2的n次方的（例如初始值为2^4=16，扩容也是以2的幂次方进行扩容，所以长度永远都是偶					数）。所以哈希表最后一个值的索引为(2^n) - 1，将(2^n) - 1转换成二进制就是n个连续的1，现在假设n=10:

​													m:h^k:    0010110111000101           0101100110110110

​													  n=10:    0000000000000000           0000001111111111

​													  m&n:    0000000000000000           0000000110110110

​					进行与运算后，实际返回的是低16位的低n（10）位，计算出来的范围就是0 ~ 2^n - 1，即0 ~ length-1的范围，和hash值对长度length取  					模计算的结果是相同的。所以哈希表长度设计成2的整次幂时，与运算操作和取模操作一样，而且对计算机来说，与运算效率更高；

​			2）源码分析

```java
// 链表与红黑树转换的阈值
static final int TREEIFY_THRESHOLD = 8;

// 最大的容量值（2^30=1073741824 < Integer.MAX_VALUE=2147483647）
static final int MAXIMUM_CAPACITY = 1 << 30;

// 初始化容量值或扩容后的容量值
// The next size value at which to resize (capacity * load factor)
int threshold;

// 定义初始容量（2^4=16）
static final int DEFAULT_INITIAL_CAPACITY = 1 << 4;

// 默认的负载因子（当容量使用率达到75%时，进行扩容操作）
static final float DEFAULT_LOAD_FACTOR = 0.75f;

// 定义一个节点数组
transient Node<K,V>[] table;

// 向Map中添加元素操作
public V put(K key, V value) {
    return putVal(hash(key), key, value, false, true);
}

/**
  * Implements Map.put and related methods.
  * @param hash hash for key
  * @param key the key
  * @param value the value to put
  * @param onlyIfAbsent if true, don't change existing value
  * 若为false同时key存在，新值覆盖旧值；true时新值不覆盖旧值，抛弃新值，保证并发情况下数据不会被覆盖；
  * @param evict if false, the table is in creation mode.
  * evict参数用于LinkedHashMap中的尾部操作，这里没有实际意义
  * @return previous value, or null if none
*/
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,boolean evict) {
    // 定义节点数组，对即将被操作的节点数组table进行引用
    Node<K,V>[] tab; 
    // 定义节点（可以理解成这是一个Entry<key,value>），即tab节点数组的某个节点
    Node<K,V> p; 
  	//n表示tab数组的长度；i表示tab数组的下标
    int n, i;
    if ((tab = table) == null || (n = tab.length) == 0){
      //判断tab节点数组为null或者tab节点数组的长度为0时，使用resize方法初始化一个节点数组，并获取初始化tab数组的长度
      n = (tab = resize()).length;
    }
  
    if ((p = tab[i = (n - 1) & hash]) == null){ 
      // 以 (n-1) 和 key的Hash值 进行与运算(&)后得到的值作为索引i（i是个节点数组中的随机位置），将tab[i]赋值给P，
      // 若P== null，说明在tab[i]的位置没有元素，以i位置为头节点的链表也不存在  
      // 以当前参数创建一个新节点，作为i位置的元素，同时作为以i为索引位置的链表头结点
      tab[i] = newNode(hash, key, value, null);
    }else {
      // p != null 说明在索引i的位置已经存在Entry元素，产生hash碰撞，开始解决hash碰撞
      // 定义一个节点e引用现在正在进行插入的Entry元素
      Node<K,V> e; 
      // 定义一个key
      K k;
      
      if (p.hash == hash && ((k = p.key) == key || (key != null && key.equals(k)))){
        // 若节点P的key的hash值当前添加的节点对应key的hash值相等(hash值相等) 且 key值相等
        // 即已存在节点的key及其对应的hash(key) 与 即将插入的节点key及其hash(key)都相等，说明key重复，进行value的值覆盖
        // 则将P节点赋值给e节点，即key已经存在，把p赋值给e，此处只是把节点引用赋值给了e，但并没有真正处理value值的覆盖
        e = p;
      }else if (p instanceof TreeNode){
        // 不相等 ，且P节点为红黑树节点，在红黑树中进行遍历是否存在相等的key，有就覆盖，没有就返回null
        e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
      }else {
        // 不在数组中，也不是红黑树类型，即处于链表节点
        for (int binCount = 0; ; ++binCount) {
          // 遍历链表，binCouunt是一个计数器，用来统计链表节点元素的个数
          if ((e = p.next) == null) {
           //若P节点没有后续节点，P节点时table[i]为头结点链表的尾结点，则直接new一个节点作为P的后续节点进行添加，设置p.next.next为null
            p.next = newNode(hash, key, value, null);
            if (binCount >= TREEIFY_THRESHOLD - 1) {
              // -1 for 1st
              // 插入成功后，链表长度是否满足了 将链表转成红黑树的阈值，若满足则执行转换，将链表转换成红黑树
              treeifyBin(tab, hash);
            }
            // 如果不满足转换成红黑树的条件，在链表中添加后元素后，直接跳出循环
            break;
          }
          if (e.hash == hash && ((k = e.key) == key || (key != null && key.equals(k)))){
            // 在链表的节点中，找到了key相等并且hash(key)也相等的Entry，则跳出循环，去第90行的执行value覆盖oldValue
            break;
          }
          // 当以上条件分支都不满足时，由于e=P.next，即e为P的洗衣歌节点元素。
          // 所以把e复制给p，此时P就成了p.next。然后再次进行循环判断，处理p.next节点。
          p = e;
        }
      }
      if (e != null) { 
        // 经过上面条件分支的处理后，此处处理key与hash(key)都相同的情况，即执行值value覆盖，不作为新元素插入
          // 1、p在节点数组中存在，把p赋值给e，然后准备执行value的覆盖
          // 2、P在链表节点中存在，将P赋值给e，然后准备执行value的覆盖
        
        // 将旧元素的value赋值给一个变量oldValue，用于数据覆盖后，旧数据value的返回
        V oldValue = e.value;
        if (!onlyIfAbsent || oldValue == null){
          // 当允许纸杯覆盖 或 旧元素的value为null时，将新添加元素的value赋值给节点e的value
          e.value = value;
        }
        // linkedHashMap的相关操作，此处暂不分析
        afterNodeAccess(e);
        // 返回旧值oldValue
        return oldValue;
      }
    }
  
  	// 计数器，记录HashMap的修改次数
    ++modCount;
  
    if (++size > threshold){
      // 作为新元素插入后，若当前HashMap中存在的节点数 大于 下次的扩容量，即达到了扩容条件，执行扩容；threshold是阈值
      resize();
    }
  	// linkedHashMap的相关操作，此处暂不分析
    afterNodeInsertion(evict);
  	//对于插入新的Entry,方法返回null
    return null;
  }

  /**
    * 初始化或者扩容一个节点数组（以2的幂次方进行扩容） 
    * Initializes or doubles table size.  If null, allocates in
    * accord with initial capacity target held in field threshold.
    * Otherwise, because we are using power-of-two expansion, the
    * elements from each bin must either stay at same index, or move
    * with a power of two offset in the new table.
    * @return the table
		*/
  final Node<K,V>[] resize() {
    --------------------- 初始化参数 ---------------------
    	// 首先使用缺省的节点数组table
      Node<K,V>[] oldTab = table;
    	// 初始化旧节点数组的容量。节点数组为null，容量为0；否则为就节点数组的长度
      int oldCap = (oldTab == null) ? 0 : oldTab.length;
    	// 初始化一个下次需要扩容的 阈值
      int oldThr = threshold;
    	// 初始化新的容量和下次需要扩容的阈值（都为0）
      int newCap, newThr = 0;
    	
    --------------------- 针对不同的情况，重新赋值节点数组的容量和节点数组下次扩容的阈值 ---------------------
      if (oldCap > 0) {
        // 由于旧节点数组的容量大于0（节点数组有元素），只需要重新赋值下次扩容的阈值
        if (oldCap >= MAXIMUM_CAPACITY) {
          // 如果oldCap的值大于节点数组默认的最大值，就将下次扩容的阈值设置为Integer的最大值(2147483647)
          threshold = Integer.MAX_VALUE;
          // 返回当前的数据
          return oldTab;
        }else if ((newCap = oldCap << 1) < MAXIMUM_CAPACITY && oldCap >= DEFAULT_INITIAL_CAPACITY) {
          // 如果旧节点数组容量的2次幂 < 2^30 并且 旧节点数组容量 > 2^4；则将旧扩容量阈值的2次幂赋值给新的扩容量阈值
          newThr = oldThr << 1;
        }
      }else if (oldThr > 0) {
        //如果旧节点数组的容量为0，则将就节点数组的下次扩容阈值赋值给容量（新）（使用下次扩容阈值作为初始化容量）
        newCap = oldThr;
      }else { 
        // 如果旧节点数组的容量和下次扩容阈值都不是大于0的，重新初始化；
        // 容量(新)为默认值2^4，下次扩容阈值为：默认的负载因子*默认容量（0.75f*16）
        newCap = DEFAULT_INITIAL_CAPACITY;
        newThr = (int)(DEFAULT_LOAD_FACTOR * DEFAULT_INITIAL_CAPACITY);
      }
      if (newThr == 0) {
        // 下次扩容容量仍是初始值0时，对其进行重新赋值
        // 根据负载因子和新的节点数组容量（newCap）计算下次的扩容量
        float ft = (float)newCap * loadFactor;
        // 若节点数组容量 < 2^30 并且 计算出的下次扩展阈值 < 2^30，则新的下次扩容阈值为按照规则计算的扩容阈值，
        // 否则赋值为Integer的最大值（因为最大容量已不满足）
        newThr = (newCap < MAXIMUM_CAPACITY && ft < (float)MAXIMUM_CAPACITY ? (int)ft : Integer.MAX_VALUE);
      }
    	// 最终结果：将新的下次扩容阈值赋值给变量threshold
      threshold = newThr;
    
    --------------------- 使用新参数初始化节点数组 ---------------------
      @SuppressWarnings({"rawtypes","unchecked"})
    	// 创建一个新的容量为newCap的节点数组，执行了扩容
      Node<K,V>[] newTab = (Node<K,V>[])new Node[newCap];
    	//将新节点数组赋值给table
      table = newTab;
      if (oldTab != null) {
        // 若旧节点数组不为null，遍历旧节点数组，复制给新桶
        for (int j = 0; j < oldCap; ++j) {
          // 初始化节点元素
          Node<K,V> e;
          if ((e = oldTab[j]) != null) {
            // 将当前索引为j的节点赋值给e（赋值给新桶），并且该节点不为null，执行将旧桶索引为j的节点置为null，释放旧链表的节点内存空间
            oldTab[j] = null;
            if (e.next == null){
            // 若索引为j的节点为尾结点（oldTab[j]为最后一个节点），重新计算下标
            // 将节点e赋值给索引A的位置(A = 元素的hash值 和 新容量-1后的值进行 与(&) 运算<只有两个数的二进制同位的数值都为1时，才为1>)
              newTab[e.hash & (newCap - 1)] = e;
            }else if (e instanceof TreeNode){
              //若原来的节点数组为红黑树，使用修剪方法进行拆分放置
              ((TreeNode<K,V>)e).split(this, newTab, j, oldCap);
            }else { 
              // lo 表示扩容后下标位置不变的链表节点
              // hi 表示扩容后下标为（原下标+原容量）的链表节点，不用重新进行哈希计算
              // 低位头结点和尾结点
              Node<K,V> loHead = null, loTail = null;
              // 高位头结点和尾结点
              Node<K,V> hiHead = null, hiTail = null;
              Node<K,V> next;
              do {
                // 循环处理桶上的链表，将链表分割成高位链表和低位链表
                // 将原来在旧桶中同一个头节点的链表，拆分成两个头结点不同的链表
                next = e.next;
                // 把原来在一个桶链表上的节点元素进行分流
                if ((e.hash & oldCap) == 0) {
                  // 桶中下标位置不变，向低位分流
                  if (loTail == null){
                    // 第一次进来，低位尾结点才为null
                    // 将e赋值给低位头结点
                    loHead = e;
                  }else{
                    //否则赋值给低位尾结点的next,即在链表尾部添加元素
                    loTail.next = e;
                  }
                  //将元素e设置为尾结点，保证下个循环能把数据链接到尾结点上
                  loTail = e;
                }else {
                  //不等于0，桶中下标位置改变，向高位分流
                  if (hiTail == null){
                    // 只有第一次进来，才null
                    // 将e赋值高位头结点
                    hiHead = e;
                  }else{
                    //将e链接在高位尾结点的next位置上
                    hiTail.next = e;
                	}
                  //将e定义为尾结点
                  hiTail = e;
                }
                //链表遍历完成的条件
              } while ((e = next) != null);
              if (loTail != null) {
                //设置低位尾结点的next为null，表示链表结束
                loTail.next = null;
                // 将低位头结点赋值给下标为j的桶数组中
                newTab[j] = loHead;
              }
              if (hiTail != null) {
                //将高位尾结点的next设置为null，表示链表结束
                hiTail.next = null;
                // 将高位头结点放置到桶中下标为（j+oldCap）的位置
                newTab[j + oldCap] = hiHead;
              }
            }
          }
        }
      }
    	//返回扩容后或者初始化的链表数组
      return newTab;
 }

final void split(HashMap<K,V> map, Node<K,V>[] tab, int index, int bit) {
  	// 将Map进行树化
    TreeNode<K,V> b = this;
    // Relink into lo and hi lists, preserving order
  	// 初始化低位的头节点和尾结点
    TreeNode<K,V> loHead = null, loTail = null;
  	// 初始化高位的头节点和尾结点
    TreeNode<K,V> hiHead = null, hiTail = null;
    int lc = 0, hc = 0;
  	// 遍历树节点
    for (TreeNode<K,V> e = b, next; e != null; e = next) {
      // 将e.next赋值给新的树next
      next = (TreeNode<K,V>)e.next;
      // 将e.next置为空
      e.next = null;
      if ((e.hash & bit) == 0) {
        if ((e.prev = loTail) == null)
          loHead = e;
        else
          loTail.next = e;
        loTail = e;
        ++lc;
      }
      else {
        if ((e.prev = hiTail) == null)
          hiHead = e;
        else
          hiTail.next = e;
        hiTail = e;
        ++hc;
      }
    }

    if (loHead != null) {
      if (lc <= UNTREEIFY_THRESHOLD)
        tab[index] = loHead.untreeify(map);
      else {
        tab[index] = loHead;
        if (hiHead != null) // (else is already treeified)
          loHead.treeify(tab);
      }
    }
    if (hiHead != null) {
      if (hc <= UNTREEIFY_THRESHOLD)
        tab[index + bit] = hiHead.untreeify(map);
      else {
        tab[index + bit] = hiHead;
        if (loHead != null)
          hiHead.treeify(tab);
      }
    }
}
```

2、获取元素（get）操作

```java
public V get(Object key) {
    Node<K,V> e;
    return (e = getNode(hash(key), key)) == null ? null : e.value;
}

final Node<K,V> getNode(int hash, Object key) {
    Node<K,V>[] tab;
  	Node<K,V> first, e; 
  	int n; 
  	K k;
    if ((tab = table) != null && (n = tab.length) > 0 && (first = tab[(n - 1) & hash]) != null) {
      	//table不为null 且 节点数组的长度大于0 且 这个key对应索引的节点不为null
        if (first.hash == hash && ((k = first.key) == key || (key != null && key.equals(k)))){
          	//若哈希值相等 且 key值相等，first就是要找的节点，直接返回
            return first;
        }
        if ((e = first.next) != null) {
          	// first不是要找的节点，找first对应链表的下一个节点（存在hash碰撞）
            if (first instanceof TreeNode){
              	// 若该节点是红黑树结构，采用红黑树对应的方法获取节点
                return ((TreeNode<K,V>)first).getTreeNode(hash, key);
            }
            do {
              	//不是红黑树，遍历链表
                if (e.hash == hash && ((k = e.key) == key || (key != null && key.equals(k)))){
                  	// 找对符合条件的节点元素，并返回
                    return e;
                }
              // 跳出循环的条件，next只要不是null，就一直执行循环遍历
            } while ((e = e.next) != null);
        }
    }
  	// 未查找到，返回null
    return null;
}
```

