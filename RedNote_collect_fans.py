import uiautomator2 as u2
import pandas as pd
import random
import time


def random_sleep(min_sec=6.0, max_sec=9.0):
    """
    Sleep for a random duration between min_sec and max_sec.
    Used to simulate human behavior and avoid detection as an automated script.
    
    在 min_sec 到 max_sec 之间随机 sleep 一段时间。
    用于模拟人类行为，避免被检测为自动脚本。

    :param min_sec: Minimum number of seconds to sleep
    :param max_sec: Maximum number of seconds to sleep
    """
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)


def get_xhs_follower_ids(user_id, max_scroll=10):
    """
    Retrieve the follower ID list of a Xiaohongshu user.
    获取小红书用户的粉丝ID列表。

    :param user_id: Xiaohongshu user ID 
        小红书用户ID
    :param max_scroll: Maximum number of scrolls to prevent infinite loops
        最大滑动次数，防止死循环
    :return: List of follower IDs
        粉丝ID列表
    """
    csv_file = f"{user_id}.csv"
    # ========== Initialization ==========
    d = u2.connect()
    random_sleep(2, 3)
    
    # ========== Launch Xiaohongshu ==========
    d.app_start("com.xingin.xhs")
    random_sleep(2, 3)
    
    # ========== Search for User ==========
    # Click on the search box
    d.xpath("//*[@resource-id='com.xingin.xhs:id/search']").click()
    random_sleep(1, 2)
    # Enter the user's ID
    for ch in user_id:
        d.send_keys(ch)
        time.sleep(0.2)  # 模拟人类打字速度
    random_sleep(1, 2)
    # Click to search
    d.xpath('//*[@text="搜索"]').click()
    random_sleep(2, 3)
    # Click the first search result
    d.xpath('//*[@resource-id="com.xingin.xhs:id/mOneBoxUserTvUsername"]').click()
    random_sleep(4, 5)
    
    # ========== Enter Homepage and Open Followers List ==========
    d.xpath('//*[@resource-id="com.xingin.xhs:id/fansLabel"]').click()
    random_sleep(3, 5)
    # d.xpath('//*[@resource-id="com.xingin.xhs:id/followLabel"]').click()
    # random_sleep(2, 3)
    # d.xpath('//*[@resource-id="com.xingin.xhs:id/tabView" and @content-desc="粉丝"]').click()
    # random_sleep(2, 3)
    
    # ========== Click "View All" if available ==========
    if d.xpath('//*[@text="查看全部"]').exists:
        d.xpath('//*[@text="查看全部"]').click()
        random_sleep(2, 3)
    
    # ========== Retrieve Followers List ==========
    scrolls = 0
    seen = set()
    fan_ids = []
    last_count = 0

    for i in range(max_scroll):
        # Number of scrolls
        if scrolls % 3 == 0 and scrolls > 0:
            # print(f"已滚动 {scrolls} 次，当前收集到 {len(fan_ids)} 个粉丝ID")
            print(f"Scrolled {scrolls} times, currently collected {len(fan_ids)} follower IDs")
            random_sleep(200, 300)
        # ========== Retrieve Each Follower Individually ==========
        followers = d.xpath('//android.view.View').all()
        for fan in followers:
            fan.click()
            random_sleep()
            fan_id = d.xpath('//*[@resource-id="com.xingin.xhs:id/profile_new_page_avatar_card_redid"]').get_text()
            fan_id = fan_id.split("：")[1].strip()
            if fan_id not in seen:
                print(fan_id)
                fan_ids.append(fan_id)
                seen.add(fan_id)
            d.press("back")
            random_sleep()
        
        # Exit early if no new followers in this round
        if len(fan_ids) == last_count:
            # print("本轮无新增粉丝ID，提前退出")
            print("No new follower IDs found this round, exiting early")
            break
        last_count = len(fan_ids)

        # Scroll down to load more
        start_x = random.randint(450, 550)
        start_y = random.randint(1600, 1800)
        end_x = start_x + random.randint(-10, 10)
        end_y = random.randint(400, 550)
        duration = random.uniform(0.3, 0.5)
        d.swipe(start_x, start_y, end_x, end_y, duration)
        scrolls += 1
        random_sleep(2, 3)
        # d(scrollable=True).scroll.vert.forward(steps=3)
        # scrolls += 1
        # random_sleep(2, 3)
    
    # ========== Save to CSV ==========
    df = pd.DataFrame({'粉丝ID': fan_ids})
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')
    
    return fan_ids


if __name__ == '__main__': 
    get_xhs_follower_ids(user_id="114765256", max_scroll=10)




