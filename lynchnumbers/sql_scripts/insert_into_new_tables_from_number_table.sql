-- Insert video into LynchVideo table
INSERT INTO lynchnumbers_lynchvideo (video)
SELECT yt_video
FROM lynchnumbers_number
ORDER BY lynchnumbers_number.date ASC;

-- Insert info into LynchVideoInfo
INSERT INTO public.lynchnumbers_lynchvideoinfo(
	"videoId",
	"publishedAt",
	"transcript",
	"number",
	"video_id"
)
SELECT 
	old_table.yt_video_id,
	old_table.date,
	old_table.yt_video_transcript,
	old_table.number,
	lynchvideo.id
FROM
	lynchnumbers_number old_table,
	lynchnumbers_lynchvideo lynchvideo
WHERE
	lynchvideo.video=old_table.yt_video
ORDER BY
	lynchvideo.id ASC;
