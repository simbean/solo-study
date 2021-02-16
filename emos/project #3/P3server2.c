#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <pthread.h> //pthread 헤더
#define SERV_IP "220.149.128.103" //서버 IP
#define SERV_PORT 4538 //서버 PORT
#define BACKLOG 10
#define INIT_MSG "==============================\nHello! I'm P2P File \n Please, LOG_IN!\n ==============================\n"
#define Success_MSG "Log-in success!!"
#define Fail_MSG "Log-in fail: Incorrect password..."
#define USER1_ID	"user1"
#define USER1_PW	"passwd1"
#define USER2_ID	"user2"
#define USER2_PW	"passwd2"
#define UI1	"==============================\nUser Information\n"
#define UI2	"==============================\n"
char msg[512]; //로그인 성공 메시지
char buf[512] = ""; //채팅 내용을 char* 형태로 저장한 변수
char chatbuf[512]; //채팅 내용에 클라이언트가 로그인한 만든 변수
int writeflag = 0; // chatbuf를 만들고 다른 클라이언트에 보내주기 위해 만든 flag(0이면 준비 안됨, 1이면 준비됨)
int sendflag = 0;
char sendmessage[512];
int new_fd; 
//char user[50];
int buffer = -1; //모든 쓰레드에서 관리되는 INDEX 값(main()문 포함)
int indexfd = -1; // 3번의 [FILE user2]등을 수행할 때 뒤의 user2가 어떤 클라이언트에서 로그인 되었는지 판별하기 위해 설정한 변수
int add[10]; //main문에서 이용할 their_addr.sin_addr.s_addr을 이용하여
//새 IP가 들어온다면 새 INDEX를 발급하여 로그인을 수행하고, 그렇지 않으면 IP가 등록된 INDEX로 로그인을 수행한다..
pthread_t controlbox; //main문에서 /help를 치면 현재 서버의 정보를 출력해주는 쓰레드
int recv_t(int socket, char* buf, int buff, int i) { //흐름 보기 위해 만든 함수
	int t;
	t = recv(socket, buf, buff, 0);
	if (t > -1) {
		//printf("recv : %d, %d\n", i, t);//받은 것이 있으면 상태를 출력해준다.
	}
	return t;
}
int send_t(int socket, char* buf, int buff, int i) {//흐름 보기 위해 만든 함수
	int t;
	t = send(socket, buf, buff, 0);
	if (t > -1) {
		//printf("send : %d, %d\n", i, t); //보낸 것이 있으면 상태를 출력해준다.
	}
}
struct client { //클라이언트의 정보를 저장하는 구조체
	int new_fd;
	int correctFlag;
	int exitFlag;
	char usingId[20];
	char address[20];
	char PORT[10];
	int waitFlag;
	pthread_t chatview; //챗을 서버에 출력하는 쓰레드
	pthread_t chatwrite; //챗을 클라이언트에 보내주는 쓰레드
	pthread_t login; //로그인 수행하는 쓰레드
};
struct client c[10]; //클라이언트의 개수는 선언부의 Thread, add와 동일한 숫자여야한다.
//최대 10개까지 소켓 가능
void cleanup(void* argu) {
	int socket = *((int*)argu);
	//printf("clean %d\n",socket);
}
void* control(void* argu) { //control 쓰레드가 수행할 함수
	char message[50];
	while (1) {
		fgets(message, sizeof(message), stdin); // /help라는 문자가 들어오면 
		if (strcmp(message, "/help\n") == 0) {
			printf("\n----------control----------\n");
			printf("buffer :\n"); //현재 서버에 들어온 클라이언트의 new_fd
			for (int i = 0; i < 10; i++) {
				printf("%d\t", c[i].new_fd);
			}
			printf("\n");
			printf("address :\n"); //주소(new_fd와 다르게 한번 들어오면 영구적으로 주소가 저장됨)
			for (int i = 0; i < 10; i++) {
				printf("Index %d : %s\n", i, c[i].address);
			}
			printf("port :\n");//PORT(new_fd와 다르게 한번 들어오면 영구적으로 주소가 저장됨)
			for (int i = 0; i < 10; i++) {
				printf("Index %d : %s\n", i, c[i].PORT);
			}
			printf("USINGID :\n"); //클라이언트가 로그인한 아이디 
			for (int i = 0; i < 10; i++) {
				printf("Index %d : %s\n", i, c[i].usingId);
			}
			//를 출력한다
		}
	}
	pthread_exit(NULL);
}

int compareWord(char* ID, char* PW, int count) { //로그인을 할 때 아이디와 비밀번호가 일치하는지 검사하는 함수
	char compareNum1[50];	
	char compareNum2[50];
	char compare[50];
	int flag = 0; //int 형 반환변수
	sprintf(compare, "%s/%s", ID, PW);
	sprintf(compareNum1, "%s/%s", USER1_ID, USER1_PW);//user1
	sprintf(compareNum2, "%s/%s", USER2_ID, USER2_PW);//user2
	if (strcmp(compare, compareNum1) == 0) {
		strcpy(c[count].usingId, USER1_ID); //user1와 일치하면 flag = 1 반환
		flag = 1;
		return flag;
	}
	else if (strcmp(compare, compareNum2) == 0) { //user2와 일치하면 flag = 2 반환
		strcpy(c[count].usingId, USER2_ID);
		flag = 2;
		return flag;
	}
	else { //일치하지 않으면 flag = 0 반환
		strcpy(c[count].usingId, ""); 
		flag = 0;
		return flag;
	}
}
char* distingish(int a, char* ID, char* PW) { //로그인 성공, 실패 메시지 출력 함수
	static char str[50] = "";
	sprintf(str, "ID: %s, PW: %s\n", ID, PW);
	if (a == 1) {
		sprintf(msg, "%s [%s] *^^*", Success_MSG, USER1_ID);
	}
	else if (a == 2) {
		sprintf(msg, "%s [%s] *^^*", Success_MSG, USER2_ID);
	}
	else sprintf(msg, "%s", Fail_MSG);
	return str;
}

int sendfile_userfound(int index) { //쓰레드 sendfile가 수행할 함수 어떤 클라이언트의 txt를 받을지 식별하는 함수
	int count = index;
	char user[20];
	int senddata = 11;
	//printf("%d", index);
	if (strcmp(buf, "[FILE-user1]\n") == 0) { 
		strcpy(user, USER1_ID);
	}
	else if (strcmp(buf, "[FILE-user2]\n") == 0) { 
		strcpy(user, USER2_ID);
	}
	else {
		strcpy(user, "NOT USER");
	}
	//user가 누군지 찾아내는 if문

	//printf("user: %s\n", user);
	for (int i = 0; i <= buffer; i++) { //현재 등록된 클라이언트 갯수만큼
		if (strcmp(user, c[i].usingId) == 0) { //아이디가 맞는지 확인하는데, 남의 클라이언트의 텍스트 파일을 받아오는 것이므로
			if (strcmp(user, c[index].usingId) != 0) { //자신이 로그인한 아이디면 안됨
				senddata = i;  //해당 클라이언트의 index를 받아옴
				break;
			}
		}
	}
	return senddata; //인덱스 반환
}

void* chatview_thread(void* argu) { //쓰레드chatview가 수행할 함수이며, 서버에 채팅을 출력하는 기능을 하는 함수
	int rcv_byte;
	int point = 0;
	int pointcount = 0;
	char message[512];
	char using[20];
	int count = *((int*)argu);
	point = c[count].new_fd; //해당 클라이언트의 new_fd
	pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, NULL);
	pthread_cleanup_push(cleanup, (void*)&point);//pthread_cancel 콜백 함수 등록
	pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);//pthread_cancel시 바로 종료
	sendflag = 0;
	//쓰레드를 로그인 쓰레드와 독립시켜 메인 쓰레드가 종료되어도 이 쓰레드는 종료되지 않게한다.
	//printf("hello viewthread %d", c[count].new_fd);
	strcpy(using, c[count].usingId); //using = 해당 클라이언트가 로그인 되었을 때 사용하는 아이디
	while (1) {		
		if (c[count].waitFlag == 0) {
			rcv_byte = recv_t(point, buf, sizeof(buf), 8);// i = 8
			if (rcv_byte > -1) { //받은것이 있다면
				writeflag = 1; //write flag 를 1로 설정해줌
				sprintf(chatbuf, "[%s] %s", using, buf); //유저 아이디와 함께 출력
				if (strcmp(buf, "\n") != 0) { //받은게 있으면
					printf("%s", chatbuf); //서버에 출력
				}
				if (strcmp(buf, ":q\n") == 0) { //만약 :q를 받으면
					c[count].exitFlag = 1; //해당 클라이언트의 exitflag를 1로 설정
					printf("bye");
					//pthread_exit(NULL);
				}
				else if (strncmp(buf, "[FILE", 5) == 0) { //만약 [FILE이 앞의 5글자에 포함되어있다면
					indexfd = sendfile_userfound(count);
					if (indexfd > -1 && indexfd < 10) {
						send_t(point, "sendmsg", 8, 131);
						sprintf(sendmessage, "SENDFILEUSERQPWOEIRUTY/%d/%s/%s\n", count, c[count].address, c[count].PORT);
						send_t(c[indexfd].new_fd, sendmessage, sizeof(sendmessage), 14);
					}
					else {
						printf("%dnot", indexfd);
						send_t(point, "sendmnsogt", 11, 132);
					}
				}
				else if (strcmp(buf, "endsend") == 0) { //만약 :q를 받으면
					indexfd = -1;
					send_t(point,"\nyou can chatting\n", 50, 9); //(채팅 메시지)
				}
			}
		}
	}
	pthread_cleanup_pop(0);
}
void* chatwrite_thread(void* argu) { //쓰레드 chatwrite 가 수행할 함수이며, 만들어진 채팅을 client에 전송하는 기능을 하는 함수
	int t;
	int point;
	int count = *((int*)argu);
	writeflag = 0;
	point = c[count].new_fd; //해당 클라이언트의 new_fd값);
	pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, NULL);
	pthread_cleanup_push(cleanup, (void*)&point);//pthread_cancel 콜백 함수 등록
	pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);//pthread_cancel시 바로 종료
	//쓰레드를 로그인 쓰레드와 독립시켜 메인 쓰레드가 종료되어도 이 쓰레드는 종료되지 않게한다.
	while (1) {
		if (writeflag == 1) {
			//chatbuf가 아무것도 없는 메시지가 아니고 위의 chatview_thread에서 만들어진 writeflag가 1일때
			if (indexfd > -1 && indexfd < 11) {
				continue;
			}
			else { //그렇지 않으면
				t = send_t(point, chatbuf, sizeof(chatbuf), 9); //i = 9(채팅 메시지를 클라이언트로 보냄)
			}
			writeflag = 0; //writeflag를 0으로 바꿈으로써, 이번 한번만 보내고 다음 메시지가 들어와 writeflag가 1이 될 때까지 대기
			strcpy(chatbuf, ""); //writeflag와 같은 이유로 초기화
		}
	}
	pthread_cleanup_pop(0);
}

void* login_thread(void* argu) { //로그인함수
	int rcv_byte;
	char idbuf[20];//id받는 변수
	char pwbuf[20];//passwd받는 변수
	char buf[512];
	char UI[512];
	char* UIstr;
	int val = *((int*)argu);
	pthread_cleanup_push(cleanup, (void*)&val);//pthread_cancel 콜백 함수 등록
	pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, NULL);
	pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);//pthread_cancel시 바로 종료
	c[val].exitFlag = 0; //exitFlag 초기화 = :q가 눌릴때까지 exitFlag는 반드시 0이어야 한다.
	rcv_byte = recv_t(c[val].new_fd, idbuf, sizeof(idbuf), 2);//i = 2 id를 받음
	send_t(c[val].new_fd, "idack", 6, 3);// i = 3 확인 신호
	rcv_byte = recv_t(c[val].new_fd, pwbuf, sizeof(pwbuf), 4);//i = 4 pw를 받음
	c[val].correctFlag = compareWord(idbuf, pwbuf, val);
	UIstr = distingish(c[val].correctFlag, idbuf, pwbuf);
	sprintf(UI, "%s%s%s", UI1, UIstr, UI2);
	printf("%s\n", UI);
	printf("msg: %s\n", msg);
	send_t(c[val].new_fd, msg, strlen(msg) + 1, 5);//i = 5 확인 신호대신 로그인 성공 메시지
	rcv_byte = recv_t(c[val].new_fd, buf, sizeof(buf), 6);//i = 6 client에서 로그인 완료 확인 신호를 받음
	strcpy(buf, "");
	if (c[val].waitFlag == 0) { //새로 들어온 클라이언트일 경우에 (3번 문제 해당)
		//c[val].waitFlag = 0;
		send_t(c[val].new_fd, "ack", 4, 7);//분기 1, i = 7 확인신호를 보냄
		rcv_byte = recv_t(c[val].new_fd, c[val].address, sizeof(c[val].address), 8);//분기 1,i = 8 클라이언트의 IP주소를 받음
		send_t(c[val].new_fd, "ack", 4, 9);//분기 1, i = 9 확인 신호를 보냄
		rcv_byte = recv_t(c[val].new_fd, c[val].PORT, sizeof(c[val].PORT), 10);//분기 1, i =10 클라이언트의 포트 번호를 받음
		if (c[val].correctFlag > 0) { //로그인 성공시
			send_t(c[val].new_fd, "chat", 5, 11);  //분기 1-1 , i = 11채팅모드를 시작하겠다는 메시지를 출력한다.
			pthread_create(&c[val].chatview, NULL, &chatview_thread, (void*)&val); //해당 클라이언트의 채팅 쓰레드 생성
			pthread_create(&c[val].chatwrite, NULL, &chatwrite_thread, (void*)&val);
		}
		else {
			send_t(c[val].new_fd, "not", 4, 11); //분기 1-2 , i = 11, 로그인 실패했다는 신호를 보낸다
		}
	}
	else { //한번 exitflag가 1이어서 나간 적이 있던 클라이언트가 다시 들어올 때
		if (c[val].correctFlag > 0) { //로그인 성공시
			send_t(c[val].new_fd, "new", 4, 70); //분기 2, i = 7 IP주소와 포트번호가 저장되어있기 때문에 굳이 보낼 필요없다는 신호를 보냄
			rcv_byte = recv_t(c[val].new_fd, buf, sizeof(buf), 80); //확인신호를 받음
			send_t(c[val].new_fd, "chat", 4, 90);//분기 2, i = 9 채팅모드 실행
			pthread_create(&c[val].chatview, NULL, &chatview_thread, (void*)&val); //해당 클라이언트의 채팅 쓰레드 생성
			pthread_create(&c[val].chatwrite, NULL, &chatwrite_thread, (void*)&val);
			c[val].waitFlag = 0;
		}
		else {
			send_t(c[val].new_fd, "new", 4, 170); //분기 2, i = 7 IP주소와 포트번호가 저장되어있기 때문에 굳이 보낼 필요없다는 신호를 보냄
			rcv_byte = recv_t(c[val].new_fd, buf, sizeof(buf), 180); //확인신호를 받음
			send_t(c[val].new_fd, "not", 4, 190); //분기 2-2, i = 7 IP주소와 포트번호가 저장되어있기 때문에 굳이 보낼 필요없다는 신호를 보냄
		}
	}
	while (1) {
		if (c[val].exitFlag == 1) { //exitflag, 즉 종료할때
			strcpy(c[val].usingId, ""); //로그인을 취소시키고
			close(c[val].new_fd); //해당 클라이언트의 new_fd소켓을 닫고
			pthread_cancel(c[val].chatview);
			pthread_cancel(c[val].chatwrite);
			c[val].new_fd = -1; //해당하는 new_fd값을 -1로 변환
			c[val].waitFlag = 1; //또한 accept 대기 플래그를 1로 만들어줌
			c[val].exitFlag = 0;
		}
		//wait
	}
	pthread_cleanup_pop(0);
}

int main(void) //accept문
{
	int sockfd;
	int flag = 0;
	struct sockaddr_in my_addr;
	struct sockaddr_in their_addr;
	unsigned int sin_size;
	int th;

	int val = 1;
	int status = -1;//중복된 주소번호일때
	//char buf[512];
	//int rcv_byte;
	sockfd = socket(AF_INET, SOCK_STREAM, 0); 
	if (sockfd == -1) {
		perror("Server-socket() error lol!");
		exit(1);
	}
	else printf("Server-socket() is OK...\n");
	my_addr.sin_family = AF_INET;
	my_addr.sin_port = htons(SERV_PORT);
	my_addr.sin_addr.s_addr = INADDR_ANY;
	memset(&(my_addr.sin_zero), 0, 8);
	if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, (char*)&val, sizeof(val)) < 0) {
		perror("setsockopt");
		close(sockfd);
		return -1;
	}

	if (bind(sockfd, (struct sockaddr*)&my_addr, sizeof(struct sockaddr)) == -1)
	{
		perror("server-bind() error lol!");
		close(sockfd);
		exit(1);
	}
	else printf("server-bind() is OK..\n");

	if (listen(sockfd, BACKLOG) == -1)
	{
		perror("listen() is error lol!");
		exit(1);
	}
	else printf("listen() is OK...\n");
	pthread_create(&controlbox, NULL, &control, (void*)&buffer); // accept전,클라이언트 상태 정보 확인하는 쓰레드 생성 
	while (1) {
		//새로운 클라이언트가 들어왔을 때 새로운 인덱스를 할당하고
		//이전 accept된 값이 한번 이상 재접속한 클라이언트일 경우
		//이전에 accept되었을 때 할당받은 인덱스를 받아야하는데,
		//만약 이때 buffer 할당받은 인덱스로 돌아가면, buffer + 1이 새로운 인덱스가 아니라면,
		//다음 accept를 수행할 때 해당 인덱스를 가진 클라이언트와 충돌한다.
		//이를 방지하기 위해 status는 새로운 인덱스를 잠시 저장한다.
		if (status != -1) { 
			buffer = status;
			status = -1; //status 초기화
		}
		sin_size = sizeof(struct sockaddr_in);
		new_fd = accept(sockfd, (struct sockaddr*)&their_addr, &sin_size);
		buffer++;//제일 처음에는 buffer가 -1이므로 -1 + 1 = 0부터 시작한다.

		for (int i = 0; i < 10; i++) {
			if (add[i] == their_addr.sin_addr.s_addr) { //클라이언트 재접속 여부 판별(재접속일 경우)
				status = buffer-1; //카운트값저장(이때 buffer는 accept가 되면 필수적으로 1을 더하기 때문에 1을 빼서 저장하여야 한다)
				pthread_cancel(c[i].login);
				buffer = i; 
				c[buffer].new_fd = new_fd; //new_fd를 이전에 할당받은 인덱스에 저장한다.
				break;
			}
			if (i == buffer) { //새로 접속일 경우
				c[buffer].new_fd = new_fd;
				break;
			}
		}
		add[buffer] = their_addr.sin_addr.s_addr;

		if (c[buffer].new_fd == -1) { //accept판별
			perror("accept() is error lol!...");
			exit(1);
		}
		else printf("accept() is OK...\n");

		send_t(c[buffer].new_fd, INIT_MSG, strlen(INIT_MSG) + 1, 1); //i = 1 환영하는 메시지 전송
		th = pthread_create(&c[buffer].login, NULL, &login_thread, (void*)&buffer); //로그인 쓰레드 생성
		if (th < 0) {
			printf("error");
		}
	}
}


